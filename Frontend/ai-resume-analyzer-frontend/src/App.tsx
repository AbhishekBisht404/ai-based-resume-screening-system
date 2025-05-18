import React, { useState } from "react";
import Header from "./components/Header";
import ResumeUpload from "./components/ResumeUpload";
import Footer from "./components/Footer";
import SideContent from "./components/SideContent";
import { Menu, X } from "lucide-react";
import './index.css';

function App() {
    const [sidebarOpen, setSidebarOpen] = useState(false);

    return (
        <div className="min-h-screen flex flex-col bg-gray-50">
            {/* Header */}
            <header className="w-full bg-black shadow-md py-4 px-8 flex items-center justify-between z-50">
                <Header />
                <button
                    className="p-2 rounded-md hover:bg-gray-200 md:hidden"
                    onClick={() => setSidebarOpen(!sidebarOpen)}
                    aria-label="Toggle sidebar"
                >
                    <Menu className="w-6 h-6 text-gray-700" />
                </button>
            </header>

            <div className="flex flex-1 overflow-hidden">
                {sidebarOpen && (
                    <aside
                        className={`
                            w-64 bg-white shadow-lg p-4 transition-transform duration-300 ease-in-out
                            ${sidebarOpen ? "translate-x-0" : "-translate-x-full"}
                            md:static md:translate-x-0 md:h-full
                        `}
                    >
                        <div className="flex justify-end mb-4 md:hidden">
                            <button
                                className="p-1 hover:bg-gray-200 rounded"
                                onClick={() => setSidebarOpen(false)}
                                aria-label="Close sidebar"
                            >
                                <X className="w-5 h-5 text-gray-600" />
                            </button>
                        </div>
                        <SideContent />
                    </aside>
                )}
                <main className="flex-1 flex items-center justify-center p-6 overflow-auto">
                    <ResumeUpload />
                </main>
            </div>
            <footer className="w-full bg-white border-t-4 border-black py-4 px-6">
                <Footer />
            </footer>
        </div>
    );
}

export default App;
