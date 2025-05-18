import React from "react";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import { Download } from "lucide-react";

interface ResumeResultProps {
    data: any;
}

const ResumeResult: React.FC<ResumeResultProps> = ({ data }) => {
    const result = data?.results?.[0];
    const score = result?.score_report;

    const toTitleCase = (str: string) => {
        return str
            .split(" ")
            .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
            .join(" ");
    };

    const formatDate = (date: Date) => {
        return date.toLocaleDateString(undefined, {
            year: "numeric",
            month: "long",
            day: "numeric",
        });
    };

    const downloadPDF = () => {
        console.log("Download PDF clicked");
        if (!result || !score) {
            console.log("No data available for PDF");
            return;
        }

        const doc = new jsPDF();

        const pageCount = doc.internal.getNumberOfPages();

        const pageWidth = doc.internal.pageSize.getWidth();
        const pageHeight = doc.internal.pageSize.getHeight();
        const margin = 14;

        const header = (pageNum: number, totalPages: number) => {
            doc.setFontSize(16);
            doc.setTextColor("#4f46e5");
            doc.setFont("helvetica", "bold");
            doc.text("Resume Analysis Report", margin, 16);
            doc.setFontSize(10);
            doc.setTextColor("#6b7280"); // Gray-500
            doc.text(`Page ${pageNum} of ${totalPages}`, pageWidth - margin - 40, 16);
            doc.setDrawColor(99, 102, 241);
            doc.setLineWidth(0.6);
            doc.line(margin, 18, pageWidth - margin, 18);
        };

        const footer = () => {
            const bottom = pageHeight - 10;
            doc.setDrawColor(220);
            doc.setLineWidth(0.3);
            doc.line(margin, bottom, pageWidth - margin, bottom);
            doc.setFontSize(10); // Increased font size for clarity
            doc.setTextColor("#1f2937"); // Darker color for better contrast
            doc.text(`Generated on ${formatDate(new Date())}`, margin, bottom + 6);
            doc.text("Resume Analysis System", pageWidth - margin - 50, bottom + 6);
        };

        header(1, 1);
        footer();

        let currentY = 26;

        doc.setFontSize(14);
        doc.setTextColor("#1f2937");
        doc.setFont("helvetica", "bold");
        doc.text("Summary & Highlights", margin, currentY);
        currentY += 8;

        doc.setFontSize(11);
        doc.setFont("helvetica", "normal");
        const summaryLines = [
            `Name: ${result.parsed_info.name || "Not Found"}`,
            `Email: ${result.parsed_info.email || "Not Found"}`,
            `Phone: ${result.parsed_info.phone || "Not Found"}`,
            `Predicted Category: ${result.score_report?.predicted_category || "Not found"}`,
            `Skill Match Score: ${score.skill_match_score} / 5`,
        ];
        summaryLines.forEach((line) => {
            doc.text(line, margin, currentY);
            currentY += 7;
        });

        currentY += 4;

        doc.setFontSize(14);
        doc.setFont("helvetica", "bold");
        doc.setTextColor("#1f2937");
        doc.text("Experience Summary", margin, currentY);
        currentY += 6;

        const experienceData = result.parsed_info.experience_summary.map((item: string, idx: number) => [ (idx+1).toString(), item ]);

        autoTable(doc, {
            startY: currentY,
            margin: { left: margin, right: margin },
            head: [["#", "Summary"]],
            body: experienceData,
            styles: {
                fontSize: 11,
                cellPadding: 4,
                valign: 'middle',
            },
            headStyles: {
                fillColor: [99, 102, 241],
                textColor: 255,
                fontStyle: "bold",
                halign: "center",
            },
            columnStyles: {
                0: { cellWidth: 12, halign: "center" },
                1: { cellWidth: 'auto' },
            },
            theme: "striped",
        });
        currentY = (doc as any).lastAutoTable.finalY + 8;

        doc.setFontSize(14);
        doc.setFont("helvetica", "bold");
        doc.setTextColor("#1f2937");
        doc.text("Skill Match Score", margin, currentY);
        currentY += 6;

        const barWidth = 150;
        const barHeight = 12;
        const barX = margin;
        const barY = currentY;

        const radius = 6;
        doc.setDrawColor("#374151");
        doc.setFillColor("#e0e7ff");

        doc.roundedRect(barX, barY, barWidth, barHeight, radius, radius, "F");

        const scorePercent = (score.skill_match_score / 5) * 100;
        const filledWidth = (scorePercent / 100) * barWidth;
        doc.setFillColor("#10b981");
        doc.roundedRect(barX, barY, filledWidth, barHeight, radius, radius, "F");

        doc.setFontSize(12);
        doc.setTextColor("#ffffff");
        const textWidth = doc.getTextWidth(`${score.skill_match_score} / 5`);
        let textX = barX + filledWidth - textWidth - 4;
        if (textX < barX + 4) textX = barX + filledWidth + 4;
        doc.text(`${score.skill_match_score} / 5`, textX, barY + barHeight - 3);

        currentY = barY + barHeight + 12;

        const matchedSkillsTitle = score.matched_skills.length
            ? score.matched_skills.map(toTitleCase).join(", ")
            : "None";
        const missingSkillsTitle = score.missing_skills.length
            ? score.missing_skills.map(toTitleCase).join(", ")
            : "None";

        const skillsTable = [
            ["Matched Skills", matchedSkillsTitle],
            ["Missing Skills", missingSkillsTitle],
        ];

        autoTable(doc, {
            startY: currentY,
            margin: { left: margin, right: margin },
            head: [["Category", "Skills"]],
            body: skillsTable,
            styles: {
                fontSize: 11,
                cellPadding: 5,
                valign: 'middle',
            },
            headStyles: {
                fillColor: [99, 102, 241],
                textColor: 255,
                fontStyle: "bold",
                halign: "center",
            },
            bodyStyles: {
                fillColor: [243, 244, 246],
                textColor: 51,
            },
            theme: "grid",
            columnStyles: {
                0: { cellWidth: 50, fontStyle: "bold" },
                1: { cellWidth: 'auto' },
            },
        });

        currentY = (doc as any).lastAutoTable.finalY + 10;

        doc.setFontSize(14);
        doc.setFont("helvetica", "bold");
        doc.setTextColor("#1f2937");
        doc.text("Skill Suggestions", margin, currentY);
        currentY += 8;

        doc.setFontSize(11);
        doc.setFont("helvetica", "italic");
        doc.setTextColor("#374151");

        Object.entries(score.skill_suggestions).forEach(([skill, suggestion]: [string, string]) => {
            const text = `${toTitleCase(skill)}: ${toTitleCase(suggestion)}`;
            const splitText = doc.splitTextToSize(text, pageWidth - 2 * margin);
            doc.text(splitText, margin, currentY);
            currentY += splitText.length * 7;

            currentY += 3;

            if (currentY > pageHeight - 30) {
                doc.addPage();
                currentY = 20;
                header(doc.internal.getNumberOfPages(), doc.internal.getNumberOfPages());
                footer();
            }
        });

        footer();

        console.log("Downloading PDF...");
        doc.save("resume_analysis_report.pdf");
    };

    if (!result || !score) {
        return (
            <div className="text-center mt-20 text-gray-600 text-lg">
                No resume analysis data found.
            </div>
        );
    }

    return (
        <div className="bg-white shadow-xl rounded-xl p-8 mt-10 space-y-8 max-w-3xl mx-auto">
            <h2 className="text-2xl font-bold text-indigo-600">Resume Analysis Report</h2>

            <div className="space-y-2">
                <h3 className="text-lg font-semibold text-gray-800">Basic Information</h3>
                <p><strong>Name:</strong> {result.parsed_info.name || "Not Found"}</p>
                <p><strong>Email:</strong> {result.parsed_info.email || "Not Found"}</p>
                <p><strong>Phone:</strong> {result.parsed_info.phone || "Not Found"}</p>
            </div>
            <p>
                <strong>Predicted Category:</strong> {result.score_report?.predicted_category || "Not found"}
            </p>
            <div className="space-y-2">
                <h3 className="text-lg font-semibold text-gray-800">Experience Summary</h3>
                <ul className="list-disc list-inside text-gray-700 text-sm">
                    {result.parsed_info.experience_summary.map((item: string, idx: number) => (
                        <li key={idx}>{item}</li>
                    ))}
                </ul>
            </div>

            <div className="mb-4">
                <h4 className="font-semibold text-gray-800">Matched Skills:</h4>
                <p className="text-green-700">
                    {score.matched_skills.length > 0
                        ? score.matched_skills.map(toTitleCase).join(", ")
                        : "None"}
                </p>
            </div>

            <div>
                <h4 className="font-semibold text-gray-800">Missing Skills:</h4>
                {score.missing_skills.length > 0 ? (
                    <ul className="list-disc list-inside text-red-700">
                        {score.missing_skills.map(skill => (
                            <li key={skill}>{toTitleCase(skill)}</li>
                        ))}
                    </ul>
                ) : (
                    <p className="text-red-700">None</p>
                )}
            </div>

            <div className="space-y-2">
                <h3 className="text-lg font-semibold text-gray-800">Skill Suggestions</h3>
                <ul className="list-disc list-inside text-gray-700 text-sm">
                    {Object.entries(score.skill_suggestions).length ? (
                        Object.entries(score.skill_suggestions).map(([skill, suggestion]) => (
                            <li key={skill}>
                                <strong>{toTitleCase(skill)}</strong>: {toTitleCase(suggestion)}
                            </li>
                        ))
                    ) : (
                        <li>No suggestions available</li>
                    )}
                </ul>
            </div>

            <div className="pt-4">
                <button
                    onClick={downloadPDF}
                    className="flex items-center gap-2 px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-lg transition duration-300 transform hover:scale-105"
                >
                    <Download className="w-5 h-5" />
                    Download PDF Report
                </button>
            </div>
        </div>
    );
};

export default ResumeResult;

