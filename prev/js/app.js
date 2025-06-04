async function generateFlowchart() {
    const idea = document.getElementById("ideaInput").value;

    const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ idea: idea })
    });

    const result = await response.json();
    const mermaidCode = result.mermaid;

    // Clean and encode
    const encoded = encodeURIComponent(mermaidCode);
    const iframeUrl = `https://mermaid.ink/img/${encoded}`;
    document.getElementById("mermaidFrame").src = iframeUrl;
}
