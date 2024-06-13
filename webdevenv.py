import os
import subprocess

def vanilla(directory):
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Vanilla Web App</title>\n</head>\n<body>\n<h1>Hello World</h1>\n</body>\n</html>')
    with open(os.path.join(directory, 'style.css'), 'w') as f:
        f.write('body {\n    font-family: Arial, sans-serif;\n}')
    with open(os.path.join(directory, 'script.js'), 'w') as f:
        f.write('console.log("Hello World");')

def php(directory):
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'index.php'), 'w') as f:
        f.write('<?php\n echo "Hello World";\n?>')
    with open(os.path.join(directory, 'style.css'), 'w') as f:
        f.write('body {\n    font-family: Arial, sans-serif;\n}')
    with open(os.path.join(directory, 'script.js'), 'w') as f:
        f.write('console.log("Hello World");')

def react(directory, project_name):
    subprocess.run(["npx", "create-react-app", project_name], cwd=directory)
    print("\nNext steps to run your React app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm start")

def nextjs(directory, project_name):
    subprocess.run(["npx", "create-next-app@latest", project_name], cwd=directory)
    print("\nNext steps to run your Next.js app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm run dev")

def remix(directory, project_name):
    subprocess.run(["npx", "create-remix@latest", project_name], cwd=directory)
    print("\nNext steps to run your Remix app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm run dev")

def gatsby(directory, project_name):
    subprocess.run(["npx", "gatsby new", project_name], cwd=directory)
    print("\nNext steps to run your Gatsby app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   gatsby develop")

def vue(directory, project_name):
    subprocess.run(["npx", "create-vue@latest", project_name], cwd=directory)
    print("\nNext steps to run your Vue app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm run serve")

def vite(directory, project_name):
    subprocess.run(["npm", "init", "vite@latest", project_name], cwd=directory)
    print("\nNext steps to run your Vite app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm run dev")

def angular(directory, project_name):
    subprocess.run(["npx", "@angular/cli", "new", project_name], cwd=directory)
    print("\nNext steps to run your Angular app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   ng serve")

def svelte(directory, project_name):
    subprocess.run(["npx", "degit", "sveltejs/template", project_name], cwd=directory)
    subprocess.run(["npm", "install"], cwd=os.path.join(directory, project_name))
    print("\nNext steps to run your Svelte app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   npm run dev")

def express(directory, project_name):
    os.makedirs(os.path.join(directory, project_name), exist_ok=True)
    subprocess.run(["npm", "init", "-y"], cwd=os.path.join(directory, project_name))
    subprocess.run(["npm", "install", "express"], cwd=os.path.join(directory, project_name))
    with open(os.path.join(directory, project_name, 'index.js'), 'w') as f:
        f.write("""
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
res.send('Hello World!');
});

app.listen(port, () => {
console.log(`Example app listening at http://localhost:${port}`);
});
""")
    print("\nNext steps to run your Express.js development environment:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the server:")
    print("   node index.js")

def flask(directory, project_name):
    os.makedirs(os.path.join(directory, project_name), exist_ok=True)
    subprocess.run(["pip", "install", "flask"], cwd=os.path.join(directory, project_name))
    with open(os.path.join(directory, project_name, 'app.py'), 'w') as f:
        f.write("""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
""")
    print("\nNext steps to run your Flask app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the Flask server:")
    print("   python app.py")

def springboot(directory, project_name):
    subprocess.run(["spring", "init", "--dependencies=web", "--build=gradle", project_name], cwd=directory)
    print("\nNext steps to run your Spring Boot app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Build the project:")
    print("   ./gradlew build")
    print("3. Run the application:")
    print("   ./gradlew bootRun")

def laravel(directory, project_name):
    subprocess.run(["composer", "create-project", "--prefer-dist", "laravel/laravel", project_name], cwd=directory)
    print("\nNext steps to run your Laravel app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   php artisan serve")

def django(directory, project_name):
    subprocess.run(["pip", "install", "django"], cwd=directory)
    subprocess.run(["django-admin", "startproject", project_name], cwd=directory)
    print("\nNext steps to run your Django app:")
    print("1. Navigate to your project directory:")
    print(f"   cd {os.path.join(directory, project_name)}")
    print("2. Start the development server:")
    print("   python manage.py runserver")

def directory():
    home_dir = os.path.expanduser("~")
    directories = {
        '1': os.path.join(home_dir, 'Desktop'),
        '2': os.path.join(home_dir, 'Documents'),
        '3': os.path.join(home_dir, 'Downloads')
    }

    print("Choose a directory to save the development environment:")
    for key, value in directories.items():
        print(f"{key}: {value}")

    choice = input("Enter the number of your choice: ")
    return directories.get(choice, home_dir)

def hello_world():
    print("##########################################")
    print("#                                        #")
    print("#          Welcome to WebDevEnv          #")
    print("#                 v0.0.0                 #")
    print("#                                        #")
    print("##########################################")
    print()
    print("Follow the prompts to name, choose the type, and select the directory of your web development environment.")
    print()

def main():
    hello_world()

    project_name = input("Enter development environment (project) name: ")

    print("Choose the type of development environment (project):")
    print("1: Vanilla (HTML/CSS/JS)")
    print("2: PHP")
    print("3: React")
    print("4: Next.js")
    print("5: Remix")
    print("6: Gatsby")
    print("7: Vue.js")
    print("8: Vite")
    print("9: Angular")
    print("10: Svelte")
    print("11: Express.js")
    print("12: Flask")
    print("13: Spring Boot")
    print("14: Laravel")
    print("15: Django")
    project_type = input("Enter the number of your choice: ")

    target_directory = directory()
    project_directory = os.path.join(target_directory, project_name)

    if project_type == '1':
        vanilla(project_directory)
        print(f'Vanilla (HTML/CSS/JS) development environment set up in: {project_directory}')
    elif project_type == '2':
        php(project_directory)
        print(f'PHP development environment set up in: {project_directory}')
    elif project_type == '3':
        react(target_directory, project_name)
        print(f'React development environment set up in: {project_directory}')
    elif project_type == '4':
        nextjs(target_directory, project_name)
        print(f'Next.js development environment set up in: {project_directory}')
    elif project_type == '5':
        remix(target_directory, project_name)
        print(f'Remix development environment set up in: {project_directory}')
    elif project_type == '6':
        gatsby(target_directory, project_name)
        print(f'Gatsby development environment set up in: {project_directory}')
    elif project_type == '7':
        vue(target_directory, project_name)
        print(f'Vue.js development environment set up in: {project_directory}')
    elif project_type == '8':
        vite(target_directory, project_name)
        print(f'Vite development environment set up in: {project_directory}')
    elif project_type == '9':
        angular(target_directory, project_name)
        print(f'Angular development environment set up in: {project_directory}')
    elif project_type == '10':
        svelte(target_directory, project_name)
        print(f'Svelte development environment set up in: {project_directory}')
    elif project_type == '11':
        express(target_directory, project_name)
        print(f'Express.js development environment set up in: {project_directory}')
    elif project_type == '12':
        flask(target_directory, project_name)
        print(f'Flask development environment set up in: {project_directory}')
    elif project_type == '13':
        springboot(target_directory, project_name)
        print(f'Spring Boot development environment set up in: {project_directory}')
    elif project_type == '14':
        laravel(target_directory, project_name)
        print(f'Laravel development environment set up in: {project_directory}')
    elif project_type == '15':
        django(target_directory, project_name)
        print(f'Django development environment set up in: {project_directory}')
    else:
        print(f'Unknown development environment type: {project_type}. Exiting.')

if __name__ == '__main__':
    main()
