export async function makeApiRequest(
  endpoint,
  method = "GET",
  body = null,
  headers = {}
) {
  const baseUrl = process.env.REACT_APP_API_URL;

  if (!baseUrl) {
    throw new Error("API base URL is not defined in REACT_APP_API_ENV");
  }

  const url = `${baseUrl}${endpoint}`;

  const defaultHeaders = {
    "Content-Type": "application/json",
    ...headers,
  };

  try {
    const response = await fetch(url, {
      method,
      headers: defaultHeaders,
      body: body ? JSON.stringify(body) : null,
    });

    if (!response.ok) {
      const errorMessage = await response.text();
      throw new Error(`API request failed: ${errorMessage}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error in makeApiRequest:", error);
    throw error;
  }
}

export async function fetchFile(endpoint, headers = {}) {
  // Get the base API URL from environment variables
  const baseUrl = process.env.REACT_APP_API_URL;

  if (!baseUrl) {
    throw new Error("API base URL is not defined in REACT_APP_API_ENV");
  }

  // Construct the full URL
  const url = `${baseUrl}${endpoint}`;

  try {
    // Fetch the file from the API
    const response = await fetch(url, {
      method: "GET",
      headers: {
        ...headers,
      },
    });

    // Check if the response status is OK
    if (!response.ok) {
      const errorMessage = await response.text();
      throw new Error(`File fetch failed: ${errorMessage}`);
    }

    // Get the file blob
    const blob = await response.blob();

    // Convert blob into a File object
    const contentDisposition = response.headers.get("content-disposition");
    let filename = "file";
    if (contentDisposition) {
      const match = contentDisposition.match(/filename="?([^"]+)"?/);
      if (match && match[1]) {
        filename = match[1];
      }
    }

    const file = new File([blob], filename, { type: blob.type });
    return file; // Return the File object
  } catch (error) {
    console.error("Error fetching file:", error);
    throw error;
  }
}
