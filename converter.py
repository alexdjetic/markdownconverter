import markdown

class Converter:
    """this class convert an markdown content to html"""
    def __init__(self, config: dict):
        self.file = config["file"]
        self.namefilehtml = config["namefilehtml"]
        self.title = config["title"]
        self.content_type = config["content_type"]
        self.content = ""

    def convert(self):
        with open(self.file, "r", encoding="utf-8") as mark:
            self.content: str = mark.read()
            self.content: str = markdown.markdown(self.content, extensions=['markdown.extensions.extra'])

    def toHtml(self):
        with open(self.namefilehtml, "w", encoding="utf-8") as html_file:
            html_file.write(f"""
            <!DOCTYPE html>\n<html>
                \n<head>\n
                    <title>{self.title}</title>\n
                    <meta http-equiv='Content-Type' content='{self.content_type}; charset=utf-8' />\n
                </head>\n
                <body>\n
                    {self.content}\n
                </body>\n
            </html>""")

        print(f"Markdown content from '{self.file}' converted to HTML and saved as '{self.namefilehtml}' with title '{self.title}' and content type '{self.content_type}'\n")

    def config(self)->str:
        return f"config: {self.file}, {self.namefilehtml}, {self.title}, {self.content_type}, {self.content}"


