import React from "react";
import { FaGithub, FaTwitter, FaLinkedin } from "react-icons/fa";

export default function Footer() {
    return (
        <footer className="w-full border-t-4 border-black bg-white py-4 px-8 text-center text-gray-600">
            <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between px-8 text-gray-700">
                <p className="text-sm">&copy; {new Date().getFullYear()} ResumeAnalyzer. All rights reserved.</p>
                <div className="flex space-x-6 mt-3 md:mt-0">
                    <a
                        href="https://github.com/your-profile"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:text-indigo-600 transition-colors"
                        aria-label="GitHub"
                    >
                        <FaGithub size={24} />
                    </a>
                    <a
                        href="https://twitter.com/your-profile"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:text-indigo-600 transition-colors"
                        aria-label="Twitter"
                    >
                        <FaTwitter size={24} />
                    </a>
                    <a
                        href="https://linkedin.com/in/your-profile"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:text-indigo-600 transition-colors"
                        aria-label="LinkedIn"
                    >
                        <FaLinkedin size={24} />
                    </a>
                </div>
            </div>
        </footer>
    );
}
