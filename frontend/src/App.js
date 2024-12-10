import React, { useState, useEffect } from "react";
import { makeApiRequest, fetchFile } from "./api-request";
import PastResume from "./components/PastResume";
import toast, { Toaster } from "react-hot-toast";

function App() {
  const [generatingResume, setGeneratingResume] = useState(false);
  const [pdfUrl, setPdfUrl] = useState(null);
  const [pastTokens, setPastTokens] = useState([]);

  const handleGenerateResume = async () => {
    try {
      setGeneratingResume(true);
      const resp = await makeApiRequest("/resumes", "POST");
      if (resp && resp.success) {
        const file = await fetchFile(`/resumes/${resp.token}`);
        const url = URL.createObjectURL(file);
        setPdfUrl(url);
        // Refresh past tokens
        getPastTokens();
      }
    } catch (e) {
      console.error(e);
      toast.error("Something went wrong generating the resume...");
    }
    setGeneratingResume(false);
  };

  async function getPastTokens() {
    try {
      const resp = await makeApiRequest("/resumes", "GET");
      setPastTokens(resp.tokens);
    } catch (e) {
      toast.error("Failed fetching past resumes");
    }
  }

  useEffect(() => {
    getPastTokens();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-full min-h-screen bg-gradient-to-b from-indigo-500 to-purple-600 text-white">
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

      {/* Section for Past Resumes */}
      <div className="mt-12 w-4/5">
        <h2 className="text-2xl font-bold mb-4">Past Resumes</h2>
        {pastTokens.length > 0 ? (
          pastTokens.map((token) => <PastResume key={token} token={token} />)
        ) : (
          <p className="text-gray-300">No past resumes found</p>
        )}
      </div>

      <Toaster />
    </div>
  );
}

export default App;
