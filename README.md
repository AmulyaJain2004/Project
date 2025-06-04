# TwinScribe

TwinScribe is a web-based tool that transforms natural language ideas into structured flowcharts, acting as a digital twin of thought processes.

## Features

- **Natural Language Processing**: Convert plain text descriptions into flowcharts
- **Dual NLP Modes**: Choose between basic and advanced text processing
- **Real-time Visualization**: See your ideas transformed instantly
- **Export Options**: Save your diagrams as SVG, PNG, or PDF
- **Intuitive Interface**: Clean, minimal design for distraction-free ideation

## How It Works

1. Enter your process, idea, or workflow as plain text
2. Select your preferred NLP mode (basic or advanced)
3. TwinScribe analyzes the text to identify steps, conditions, and branches
4. A visual flowchart is automatically generated using MermaidJS
5. View, edit, or export your diagram in various formats

## Usage Examples

TwinScribe works best with text that includes clear sequences and conditional logic. For example:

```
Start with checking email. If there are new messages, read and respond to them, otherwise continue. Next, review my calendar. If there are meetings, prepare for them, otherwise work on pending tasks.
```

## NLP Modes

- **Basic Mode**: Uses simple pattern matching to identify conditions and sequences
- **Advanced Mode**: Uses the Compromise.js library for more sophisticated natural language processing, capable of better understanding complex sentences and relationships

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Diagram Rendering**: MermaidJS
- **Natural Language Processing**: 
  - Custom pattern-based parsing
  - Compromise.js library
- **Export Formats**: SVG, PNG, PDF (using jsPDF and html2canvas)

## Getting Started

1. Clone this repository
2. Open `index.html` in your web browser
3. Start converting your ideas into flowcharts!

## Future Enhancements

- Advanced NLP with additional libraries
- User accounts and diagram storage
- Collaborative editing
- Custom styling options for diagrams

## License

MIT License