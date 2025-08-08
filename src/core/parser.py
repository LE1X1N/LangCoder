from src.tmpl import TemplateManager


class DataParser:
    def __init__(self, tmpl_manager: TemplateManager):
        self.tmpl_manager = tmpl_manager

    def parse(self, data: dict, request_id: str) -> list:
        # Parse JSON into tasks list
        tasks = []
        for mid, module in enumerate(data["web_pages"]):
            for pid, page in enumerate(module['page']):
                tasks.append(
                    {
                        "request_id" : request_id,
                        "page_id" : f'{mid}_{pid}',
                        "web_title": data["title"], 
                        "web_detail": data["page_detail"] ,
                        "module_name": module["page_name"],
                        "page_name": page["name"],
                        "page_desc": page["text"],
                        "page_tmpl": self.tmpl_manager.load_template(int(module["style"]))
                    }
                )
                
        return tasks