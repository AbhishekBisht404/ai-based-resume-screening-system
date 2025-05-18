import React from "react";
import { FaUserTie } from "react-icons/fa";

export default function Header() {
    return (
        <div className="flex items-center justify-center max-w-7xl mx-auto">
            {/* Logo or Brand */}
            <div className="flex items-center space-x-2">
                <FaUserTie className="text-indigo-600 text-3xl" />
                <h1 className="text-xl font-bold text-gray-800">AI Resume Analyzer</h1>
            </div>

            {/* Navigation or Menu Icon */}
        </div>
    );
}
