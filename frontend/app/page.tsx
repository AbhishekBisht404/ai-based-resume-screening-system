import ResumeForm from "./components/ResumeForm";

export default function Home() {
  return (
      <main className="flex flex-col items-center justify-center min-h-screen p-6">
        <h1 className="text-3xl font-bold mb-6">AI Resume Analyzer</h1>
        <ResumeForm />
      </main>
  );
}
