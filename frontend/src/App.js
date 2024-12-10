import React, { useState } from "react";
import { makeApiRequest, fetchFile } from "./api-request";
import toast, { Toaster } from "react-hot-toast";

function App() {
  const [generatingResume, setGeneratingResume] = useState(false);
  const [pdfUrl, setPdfUrl] = useState(null);

  const handleGenerateResume = async () => {
    try {
      setGeneratingResume(true);
      const resp = await makeApiRequest("/resume", "POST");
      if (resp && resp.success) {
        const file = await fetchFile(`/resume/${resp.token}`);
        const url = URL.createObjectURL(file);
        setPdfUrl(url);
      }
    } catch (e) {
      console.error(e);
      toast.error("Something went wrong generating the resume...");
    }
    setGeneratingResume(false);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-b from-indigo-500 to-purple-600 text-white">
      <h1 className="text-4xl font-bold mb-4 z-10">CSC 482 Resume Generator</h1>

      <button
        onClick={handleGenerateResume}
        className="px-6 py-3 bg-yellow-500 text-indigo-900 font-bold rounded-lg shadow-md hover:bg-yellow-600 transition z-10"
      >
        {generatingResume ? "Generating..." : "Generate Resume"}
      </button>
      {pdfUrl && (
        <div className="mt-6 w-full flex justify-center">
          <iframe
            src={pdfUrl}
            title="Resume PDF"
            className="border rounded-md"
            style={{ width: "80%", height: "500px" }}
          />
        </div>
      )}
      <Toaster />
    </div>
  );
}

export default App;
