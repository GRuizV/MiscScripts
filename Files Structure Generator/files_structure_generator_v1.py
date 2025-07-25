import os

def generate_markdown_tree(start_path, output_file):

    def walk_dir(path, prefix=""):

        entries = sorted(os.listdir(path))
        entries = [e for e in entries if not e.startswith(".")]  # skip hidden files
        result = []

        for index, entry in enumerate(entries):

            full_path = os.path.join(path, entry)

            connector = "└──" if index == len(entries) - 1 else "├──"

            if os.path.isdir(full_path):
                
                result.append(f"{prefix}{connector} 📁 {entry}")
                extension = "    " if index == len(entries) - 1 else "│   "
                result += walk_dir(full_path, prefix + extension)

            else:
                result.append(f"{prefix}{connector} 📄 {entry}")

        return result

    tree_lines = [f"📁 {os.path.basename(start_path) or start_path}/"]
    tree_lines += walk_dir(start_path)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))

    print(f"✅ Markdown document map saved to: {output_file}")


# 👉 Configure this path to your actual Nima Cloud folder
nima_cloud_path = r"C:\Users\USUARIO\OneDrive\Nima Cloud"
output_md_path = os.path.join(nima_cloud_path, "Nima_Cloud_Document_Map.md")

generate_markdown_tree(nima_cloud_path, output_md_path)