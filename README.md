# Airport CLI

A command-line interface tool that makes directory navigation easy through intelligent fuzzy search functionality.

## 🚀 Features

- **Fuzzy Directory Search**: Find directories using partial names with intelligent matching
- **Levenshtein Distance Algorithm**: Advanced string matching that handles typos and abbreviations
- **Interactive Navigation**: Simple prompts to guide you to your destination directory
- **Automatic Directory Change**: Seamlessly changes to the matched directory and opens a new bash session
- **Unix Find Integration**: Efficiently traverses directory trees to locate targets

## 📦 Installation

### From Source
```bash
git clone https://github.com/ali-abdullah/airport
cd airport
pip install -e .
```

### Using pip
```bash
pip install airport
```

## 🔧 Usage

### Basic Commands

Display help information:
```bash
airport --help
```

Show version:
```bash
airport --version
```

List and navigate directories:
```bash
airport listdir
```

The tool will prompt you to enter a directory name. You can type:
- Full directory names
- Partial directory names  
- Names with typos (the fuzzy matching will find the closest match)

### Example Workflow
```bash
$ airport listdir
Directory: proj
# The tool will find the best match for "proj" (e.g., "Projects")
# and automatically change to that directory in a new bash session
```

## 🛠️ Technical Details

### Architecture
- **Base Command System**: Extensible command structure using inheritance
- **Fuzzy Matching Engine**: Custom implementation using Levenshtein distance
- **CLI Framework**: Built with docopt for robust argument parsing

### Dependencies
- `docopt`: Command-line interface creation
- Python 2.7+ (Note: This project uses legacy Python syntax)

### Algorithm
The fuzzy search uses a combination of:
1. **Levenshtein Distance**: Calculates edit distance between strings
2. **Position-based Scoring**: Considers character position matches
3. **Weighted Scoring**: Balances edit distance with positional accuracy

## 🔄 Development

### Project Structure
```
airport/
├── airport/
│   ├── __init__.py          # Package initialization and version
│   ├── cli.py               # Main CLI entry point
│   └── commands/            # Command modules
│       ├── __init__.py
│       ├── base.py          # Base command class
│       └── listdir.py       # Directory listing command
├── setup.py                 # Package configuration
├── LICENSE                  # MIT License
└── README.md               # This file
```

### Running Tests
```bash
pip install -e .[test]
pytest
```

## 📋 Requirements

- Python 2.7+
- Unix-like operating system (Linux, macOS)
- Bash shell

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ali Abdullah**
- Email: ali.abdullah.salahuddin@gmail.com
- GitHub: [@ali-abdullah](https://github.com/ali-abdullah)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Version History

- **v0.1**: Initial release with basic fuzzy directory search functionality

---

*Airport CLI - Navigate your filesystem like a pilot navigates airports* ✈️
