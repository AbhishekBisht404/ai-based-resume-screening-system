"use client";
import { useState } from "react";

export default function ResumeForm() {
    const [selectedJob, setSelectedJob] = useState<string>("");
    const [file, setFile] = useState<File | null>(null);
    const [response, setResponse] = useState<any>(null);

    const jobRoles = [
        "Software Engineer",
        "Web Developer",
        "Data Scientist",
        "DevOps Engineer",
        "Cybersecurity Analyst",
        "UI/UX Designer",
    ];

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!file || !selectedJob) {
            alert("Please select a job role and upload a resume.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);
        formData.append("job_role", selectedJob);

        try {
            const res = await fetch("http://localhost:8000/analyze_resume/", {
                method: "POST",
                body: formData,
            });
            const data = await res.json();
            setResponse(data);
        } catch (error) {
            console.error("Error uploading file:", error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit} className="mb-6">
                <label className="block font-semibold mb-2">Select Job Role:</label>
                <select
                    className="border p-2 w-full mb-4"
                    value={selectedJob}
                    onChange={(e) => setSelectedJob(e.target.value)}
                >
                    <option value="">-- Select a Job Role --</option>
                    {jobRoles.map((role) => (
                        <option key={role} value={role}>
                            {role}
                        </option>
                    ))}
                </select>

                <label className="block font-semibold mb-2">Upload Resume:</label>
                <input
                    type="file"
                    accept=".pdf, .docx"
                    className="border p-2 w-full mb-4"
                    onChange={(e) => setFile(e.target.files[0])}
                />

                <button
                    type="submit"
                    className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700"
                >
                    Analyze Resume
                </button>
            </form>

            {response && (
                <div className="bg-gray-50 p-4 rounded-md shadow-md">
                    <h2 className="text-lg font-bold">Results</h2>
                    <p><strong>Predicted Job Role:</strong> {response["Predicted Job Role"]}</p>
                    <p><strong>Selected Job Role:</strong> {response["Selected Job Role"]}</p>
                    <p><strong>Resume Score:</strong> {response["Resume Score"]}%</p>
                    <p><strong>Extracted Skills:</strong> {response["Extracted Skills"].join(", ")}</p>
                    {response["Missing Skills"].length > 0 ? (
                        <p><strong>Missing Skills:</strong> {response["Missing Skills"].join(", ")}</p>
                    ) : (
                        <p className="text-green-600"><strong>No Missing Skills! 🚀</strong></p>
                    )}
                    <p className="mt-2 text-blue-500 font-semibold">{response["Suggestions"]}</p>
                </div>
            )}
        </div>
    );
}
