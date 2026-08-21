import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# The section starts with <!-- ═══════════════════════════════════════\n         APPLICATION CATEGORIES
# and ends with </section>
pattern = re.compile(r'    <!-- ═══════════════════════════════════════\n         APPLICATION CATEGORIES\n    ═══════════════════════════════════════ -->\n    <section class="section-categories" id="categories">.*?</section>\n', re.DOTALL)
match = pattern.search(content)

if not match:
    print("Section not found in index.html")
else:
    section_text = match.group(0)
    
    # Remove from index.html
    new_content = content.replace(section_text, "")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Removed from index.html")

    # Insert into about.html
    with open("about.html", "r", encoding="utf-8") as f:
        about_content = f.read()

    # The owner info starts with:
    #     <!-- ═══════════════════════════════════════
    #          FOUNDER / ABOUT SECTION
    target_pattern = r'    <!-- ═══════════════════════════════════════\n         FOUNDER / ABOUT SECTION'
    
    if target_pattern.replace("\\n", "\n") in about_content:
        target_str = target_pattern.replace("\\n", "\n")
        new_about_content = about_content.replace(target_str, section_text + "\n" + target_str)
        with open("about.html", "w", encoding="utf-8") as f:
            f.write(new_about_content)
        print("Inserted into about.html")
    else:
        print("Target insertion point not found in about.html")
