# Folder.Visualizer
# Project Structure Visualizer

A Python tool to visualize the folder structure of any project directory with a beautiful tree-like representation. Perfect for documenting project architecture or understanding the organization of .NET, Angular, React, C#, or any other framework projects.

## Features

- 🌳 **Tree Visualization**: Clean, hierarchical display of your project structure
- 🎯 **Smart Filtering**: Automatically ignores common build artifacts and dependencies
- 🔧 **Customizable**: Configure depth limits, ignore patterns, and output options
- 📁 **Flexible**: Show files, directories only, or include hidden items
- 💾 **Export Ready**: Output to console or save to file for documentation

## Installation

1. Clone this repository or download the `Folder.Visualizer.py` file
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required!

```bash
# Clone the repository
git clone https://github.com/crazilazi/Folder.Visualizer.git
cd Folder.Visualizer

# Or download directly
wget https://raw.githubusercontent.com/crazilazi/project-structure-visualizer/main/Folder.Visualizer.py
```

## Usage

### Basic Usage

```bash
# Visualize current directory
python Folder.Visualizer.py

# Visualize a specific directory
python Folder.Visualizer.py -d /path/to/your/project

# Save output to a file
python Folder.Visualizer.py -d /path/to/your/project -o structure.txt
```

### Advanced Options

```bash
# Ignore specific patterns
python Folder.Visualizer.py -i "*.log" -i "temp_*"

# Limit depth to 2 levels
python Folder.Visualizer.py -m 2

# Show only directories (no files)
python Folder.Visualizer.py -n

# Include hidden files and directories
python Folder.Visualizer.py --include-hidden
```

### Command Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--directory` | `-d` | Root directory to visualize (default: current directory) |
| `--output` | `-o` | Output file path (default: print to console) |
| `--ignore` | `-i` | Patterns to ignore (can be used multiple times) |
| `--max-depth` | `-m` | Maximum depth to traverse |
| `--no-files` | `-n` | Show only directories, exclude files |
| `--include-hidden` | | Include hidden files and directories |

## Example Output

### React Project Structure
```
my-react-app/
├── public/
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── Button.js
│   │   ├── Header.js
│   │   └── Navbar.js
│   ├── hooks/
│   │   └── useAuth.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package.json
├── package-lock.json
└── README.md
```

### .NET Core Project Structure
```
MyWebApp/
├── Controllers/
│   ├── HomeController.cs
│   └── ApiController.cs
├── Models/
│   ├── User.cs
│   └── Product.cs
├── Views/
│   ├── Home/
│   │   ├── Index.cshtml
│   │   └── Privacy.cshtml
│   └── Shared/
│       └── _Layout.cshtml
├── wwwroot/
│   ├── css/
│   ├── js/
│   └── images/
├── appsettings.json
├── Program.cs
└── MyWebApp.csproj
```

### Angular Project Structure
```
my-angular-app/
├── src/
│   ├── app/
│   │   ├── components/
│   │   ├── services/
│   │   ├── app.component.ts
│   │   ├── app.component.html
│   │   └── app.module.ts
│   ├── assets/
│   ├── environments/
│   ├── index.html
│   └── main.ts
├── angular.json
├── package.json
└── tsconfig.json
```

## Automatically Ignored Directories

The tool automatically ignores common build artifacts and dependencies:

- `node_modules/` - Node.js dependencies
- `.git/` - Git version control
- `.vs/` - Visual Studio files
- `__pycache__/` - Python cache
- `bin/` & `obj/` - .NET build outputs
- `dist/` & `build/` - Build directories
- `.vscode/` & `.idea/` - IDE configuration

## Use Cases

- 📋 **Documentation**: Generate project structure for README files
- 🔍 **Code Reviews**: Quickly understand project organization
- 📊 **Architecture Analysis**: Visualize large codebases
- 🎓 **Learning**: Explore how different frameworks organize projects
- 📝 **Project Planning**: Plan directory structures for new projects

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find this tool helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs by opening an issue
- 💡 Suggesting new features
- 📢 Sharing with your team

---

**Made with ❤️ for developers who love clean, organized code structures**
