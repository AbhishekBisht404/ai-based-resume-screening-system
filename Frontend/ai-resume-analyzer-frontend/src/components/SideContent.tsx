import React from "react";
import { FaRegFileAlt, FaBullseye, FaRocket } from "react-icons/fa";

export default function SideContent() {
    return (
        <aside className="w-80 bg-gray-50 p-6 rounded-lg shadow-lg ml-8 text-gray-800 max-h-screen overflow-y-auto">
            <h2 className="text-2xl font-semibold mb-6 text-indigo-600">Career Tips & Best Practices</h2>

            <section className="mb-6">
                <h3 className="flex items-center text-lg font-semibold mb-2 text-indigo-700">
                    <FaRegFileAlt className="mr-2 text-2xl" /> Resume Tips
                </h3>
                <ul className="list-disc list-inside space-y-2 text-sm text-gray-700">
                    <li className="hover:text-indigo-600 transition-colors duration-200">Keep your resume concise — ideally 1 page.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Use bullet points for readability.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Tailor your resume to each job description.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Highlight measurable achievements.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Avoid generic phrases like "hardworking" without proof.</li>
                </ul>
            </section>

            <section className="mb-6">
                <h3 className="flex items-center text-lg font-semibold mb-2 text-indigo-700">
                    <FaBullseye className="mr-2 text-2xl" /> How to Stand Out
                </h3>
                <ul className="list-disc list-inside space-y-2 text-sm text-gray-700">
                    <li className="hover:text-indigo-600 transition-colors duration-200">Use action verbs: “Led”, “Developed”, “Increased”.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Include relevant keywords for ATS.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Use a clean, professional layout.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Proofread to avoid typos.</li>
                </ul>
            </section>

            <section>
                <h3 className="flex items-center text-lg font-semibold mb-2 text-indigo-700">
                    <FaRocket className="mr-2 text-2xl" /> Ready to Level Up?
                </h3>
                <ul className="list-disc list-inside space-y-2 text-sm text-gray-700">
                    <li className="hover:text-indigo-600 transition-colors duration-200">Regularly update your skills.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Get feedback from peers or mentors.</li>
                    <li className="hover:text-indigo-600 transition-colors duration-200">Practice interview questions alongside resume prep.</li>
                </ul>
            </section>
        </aside>
    );
}
