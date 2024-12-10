import React, { useState } from "react";
import { fetchFile } from "../api-request";
import toast from "react-hot-toast";

const PastResume = ({ token }) => {
  const [pdfUrl, setPdfUrl] = useState(null);
  const [showPdf, setShowPdf] = useState(false);

  const handleFetchResume = async () => {
    try {
      const file = await fetchFile(`/resumes/${token}`);
      const url = URL.createObjectURL(file);
      setPdfUrl(url);
      setShowPdf(true);
    } catch (e) {
      console.error(e);
      toast.error("Failed to fetch the resume");
    }
  };

  const togglePdfVisibility = () => {
    setShowPdf((prev) => !prev);
  };

  return (
    <div className="bg-gray-800 bg-opacity-75 p-4 rounded-lg shadow-md mb-4 text-white w-full">
      <div className="flex justify-between items-center">
        <span className="font-bold">Resume Token: {token}</span>
        <div>
          {!pdfUrl && (
            <button
              onClick={handleFetchResume}
              className="px-4 py-2 bg-blue-500 rounded-lg hover:bg-blue-600 transition text-sm"
            >
              Fetch Resume
            </button>
          )}
          {pdfUrl && (
            <button
              onClick={togglePdfVisibility}
              className={`px-4 py-2 rounded-lg transition text-sm ${
                showPdf
                  ? "bg-red-500 hover:bg-red-600"
                  : "bg-green-500 hover:bg-green-600"
              }`}
            >
              {showPdf ? "Hide PDF" : "Show PDF"}
            </button>
          )}
        </div>
      </div>
      {showPdf && pdfUrl && (
        <iframe
          src={pdfUrl}
          title={`Resume ${token}`}
          className="border rounded-md mt-4"
          style={{ width: "100%", height: "400px" }}
        />
      )}
    </div>
  );
};

export default PastResume;
