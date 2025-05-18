import React, { useState } from "react";
import { Box, Button, Typography, CircularProgress, Alert } from "@mui/material";
import UploadFileIcon from "@mui/icons-material/UploadFile";

import ResumeResult from "./ResumeResult";

export default function ResumeUpload() {
    const [file, setFile] = useState<File | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [resultData, setResultData] = useState<any | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setError(null);
        setResultData(null);
        const selectedFile = event.target.files?.[0] || null;
        if (selectedFile && selectedFile.type !== "application/pdf") {
            setError("Please upload a PDF file only.");
            setFile(null);
            return;
        }
        setFile(selectedFile);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setError(null);
        setResultData(null);

        if (!file) {
            setError("Please select a PDF file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", file);

        setLoading(true);
        try {
            const response = await fetch("http://localhost:8000/api/analyze_resumes", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.statusText}`);
            }

            const data = await response.json();
            setResultData(data);
            setFile(null);
        } catch (err: any) {
            setError(err.message || "Failed to upload file. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box
            sx={{
                width: 400,
                bgcolor: "background.paper",
                p: 4,
                borderRadius: 3,
                boxShadow: 6,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
            }}
        >
            <Typography variant="h6" mb={2}>
                Upload your resume (PDF only)
            </Typography>

            <Button
                variant="contained"
                component="label"
                startIcon={<UploadFileIcon />}
                sx={{ mb: 2, width: "100%" }}
            >
                {file ? file.name : "Choose File"}
                <input
                    type="file"
                    accept="application/pdf"
                    hidden
                    onChange={handleFileChange}
                />
            </Button>

            {error && (
                <Alert severity="error" sx={{ mb: 2, width: "100%" }}>
                    {error}
                </Alert>
            )}

            <Button
                variant="contained"
                color="primary"
                onClick={handleSubmit}
                disabled={loading || !file}
                fullWidth
                size="large"
            >
                {loading ? <CircularProgress size={24} color="inherit" /> : "Analyze Resume"}
            </Button>

            {resultData && (
                <Box mt={4} width="100%">
                    <ResumeResult data={resultData} />
                </Box>
            )}
        </Box>
    );
}
