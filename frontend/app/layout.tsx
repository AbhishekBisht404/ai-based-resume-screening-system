import { ReactNode } from "react";
import "./globals.css";

export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="en">
        <body className="bg-gray-100">
        <div className="container mx-auto p-6">{children}</div>
        </body>
        </html>
    );
}
