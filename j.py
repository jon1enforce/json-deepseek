#!/usr/bin/env python3
import json
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import sys
import os

class JSONViewer:
    def __init__(self, filename):
        self.filename = filename
        self.modified = False
        self.dark_mode = False
        self.language = "en"  # Default: English
        
        # Sprachdefinitionen
        self.translations = {
            "de": self.get_german_translations(),
            "en": self.get_english_translations(),
            "es": self.get_spanish_translations(),
            "zh": self.get_chinese_translations(),
            "ja": self.get_japanese_translations(),
            "ko": self.get_korean_translations()
        }
        
        if self.load_json():
            self.setup_gui()
    
    def get_german_translations(self):
        return {
            "title": "JSON Editor",
            "structure": "📁 JSON Struktur",
            "raw_editor": "📝 Raw JSON Editor", 
            "templates": "🚀 Schnell-Templates",
            "add": "➕ Hinzufügen",
            "edit": "✏️ Bearbeiten",
            "delete": "🗑️ Löschen",
            "search": "🔍 Suchen",
            "save": "💾 Speichern",
            "reload": "🔄 Neu laden",
            "validate": "✅ Validieren",
            "format": "🧹 Formatieren",
            "ready": "✅ Bereit",
            "modified": "✏️ Geändert",
            "saved": "✅ Gespeichert",
            "project_spec": "📋 Projekt Spec",
            "api_design": "🔌 API Design",
            "test_cases": "🧪 Test Cases",
            "config": "⚙️ Config",
            "data_model": "📊 Datenmodell",
            "settings": "⚙️ Einstellungen",
            "dark_mode": "🌙 Dark Mode",
            "language": "🌐 Sprache",
            "file_not_found": "Datei nicht gefunden",
            "syntax_error": "JSON Syntax Fehler",
            "save_success": "Datei erfolgreich gespeichert!",
            "validation_ok": "✅ JSON ist syntaktisch korrekt!",
            "validation_error": "❌ JSON Fehler",
            "unsaved_changes": "Ungespeicherte Änderungen",
            "confirm_close": "Ungespeicherte Änderungen gehen verloren. Wirklich schließen?",
            "confirm_reload": "Ungespeicherte Änderungen gehen verloren. Fortfahren?",
            "confirm_delete": "Wirklich löschen?",
            "select_node": "Bitte wählen Sie einen Knoten aus!",
            "select_item": "Bitte wählen Sie einen Eintrag aus!",
            "key_prompt": "Schlüssel/Name:",
            "type_prompt": "Typ (string/number/boolean/object/array):",
            "value_prompt": "Wert:",
            "search_prompt": "Suchbegriff:",
            "template_prompt": "Template Name:",
            "edit_prompt": "Aktueller Wert: {}\nNeuer Wert:",
            "context_add": "➕ Hinzufügen",
            "context_edit": "✏️ Bearbeiten", 
            "context_delete": "🗑️ Löschen",
            "context_copy": "📋 In Editor kopieren",
            "context_scroll": "🎯 Zu diesem Punkt scrollen",
            "object_edit_info": "Objekte und Arrays können nur über Raw-Editor bearbeitet werden.",
            "tree_key": "Schlüssel / Eigenschaft",
            "tree_type": "Typ",
            "tree_value": "Wert"
        }
    
    def get_english_translations(self):
        return {
            "title": "JSON Editor",
            "structure": "📁 JSON Structure", 
            "raw_editor": "📝 Raw JSON Editor",
            "templates": "🚀 Quick Templates",
            "add": "➕ Add",
            "edit": "✏️ Edit",
            "delete": "🗑️ Delete",
            "search": "🔍 Search",
            "save": "💾 Save",
            "reload": "🔄 Reload",
            "validate": "✅ Validate",
            "format": "🧹 Format",
            "ready": "✅ Ready",
            "modified": "✏️ Modified",
            "saved": "✅ Saved",
            "project_spec": "📋 Project Spec",
            "api_design": "🔌 API Design",
            "test_cases": "🧪 Test Cases",
            "config": "⚙️ Config",
            "data_model": "📊 Data Model",
            "settings": "⚙️ Settings",
            "dark_mode": "🌙 Dark Mode",
            "language": "🌐 Language",
            "file_not_found": "File not found",
            "syntax_error": "JSON Syntax Error",
            "save_success": "File saved successfully!",
            "validation_ok": "✅ JSON is syntactically correct!",
            "validation_error": "❌ JSON Error",
            "unsaved_changes": "Unsaved changes",
            "confirm_close": "Unsaved changes will be lost. Really close?",
            "confirm_reload": "Unsaved changes will be lost. Continue?",
            "confirm_delete": "Really delete?",
            "select_node": "Please select a node!",
            "select_item": "Please select an item!",
            "key_prompt": "Key/Name:",
            "type_prompt": "Type (string/number/boolean/object/array):",
            "value_prompt": "Value:",
            "search_prompt": "Search term:",
            "template_prompt": "Template name:",
            "edit_prompt": "Current value: {}\nNew value:",
            "context_add": "➕ Add",
            "context_edit": "✏️ Edit",
            "context_delete": "🗑️ Delete",
            "context_copy": "📋 Copy to editor",
            "context_scroll": "🎯 Scroll to this point",
            "object_edit_info": "Objects and arrays can only be edited via Raw Editor.",
            "tree_key": "Key / Property",
            "tree_type": "Type", 
            "tree_value": "Value"
        }
    
    def get_spanish_translations(self):
        return {
            "title": "Editor JSON",
            "structure": "📁 Estructura JSON",
            "raw_editor": "📝 Editor JSON Raw",
            "templates": "🚀 Plantillas Rápidas",
            "add": "➕ Añadir",
            "edit": "✏️ Editar",
            "delete": "🗑️ Eliminar",
            "search": "🔍 Buscar",
            "save": "💾 Guardar",
            "reload": "🔄 Recargar",
            "validate": "✅ Validar",
            "format": "🧹 Formatear",
            "ready": "✅ Listo",
            "modified": "✏️ Modificado",
            "saved": "✅ Guardado",
            "project_spec": "📋 Especificación Proyecto",
            "api_design": "🔌 Diseño API",
            "test_cases": "🧪 Casos Prueba",
            "config": "⚙️ Configuración",
            "data_model": "📊 Modelo Datos",
            "settings": "⚙️ Ajustes",
            "dark_mode": "🌙 Modo Oscuro",
            "language": "🌐 Idioma",
            "file_not_found": "Archivo no encontrado",
            "syntax_error": "Error de sintaxis JSON",
            "save_success": "¡Archivo guardado exitosamente!",
            "validation_ok": "✅ ¡JSON es sintácticamente correcto!",
            "validation_error": "❌ Error JSON",
            "unsaved_changes": "Cambios no guardados",
            "confirm_close": "Los cambios no guardados se perderán. ¿Realmente cerrar?",
            "confirm_reload": "Los cambios no guardados se perderán. ¿Continuar?",
            "confirm_delete": "¿Realmente eliminar?",
            "select_node": "¡Por favor seleccione un nodo!",
            "select_item": "¡Por favor seleccione un elemento!",
            "key_prompt": "Clave/Nombre:",
            "type_prompt": "Tipo (string/number/boolean/object/array):",
            "value_prompt": "Valor:",
            "search_prompt": "Término de búsqueda:",
            "template_prompt": "Nombre plantilla:",
            "edit_prompt": "Valor actual: {}\nNuevo valor:",
            "context_add": "➕ Añadir",
            "context_edit": "✏️ Editar",
            "context_delete": "🗑️ Eliminar",
            "context_copy": "📋 Copiar al editor",
            "context_scroll": "🎯 Desplazar a este punto",
            "object_edit_info": "Objetos y arrays solo pueden editarse mediante Editor Raw.",
            "tree_key": "Clave / Propiedad",
            "tree_type": "Tipo",
            "tree_value": "Valor"
        }
    
    def get_chinese_translations(self):
        return {
            "title": "JSON 编辑器",
            "structure": "📁 JSON 结构",
            "raw_editor": "📝 原始 JSON 编辑器",
            "templates": "🚀 快速模板",
            "add": "➕ 添加",
            "edit": "✏️ 编辑",
            "delete": "🗑️ 删除",
            "search": "🔍 搜索",
            "save": "💾 保存",
            "reload": "🔄 重新加载",
            "validate": "✅ 验证",
            "format": "🧹 格式化",
            "ready": "✅ 就绪",
            "modified": "✏️ 已修改",
            "saved": "✅ 已保存",
            "project_spec": "📋 项目规范",
            "api_design": "🔌 API 设计",
            "test_cases": "🧪 测试用例",
            "config": "⚙️ 配置",
            "data_model": "📊 数据模型",
            "settings": "⚙️ 设置",
            "dark_mode": "🌙 暗黑模式",
            "language": "🌐 语言",
            "file_not_found": "文件未找到",
            "syntax_error": "JSON 语法错误",
            "save_success": "文件保存成功！",
            "validation_ok": "✅ JSON 语法正确！",
            "validation_error": "❌ JSON 错误",
            "unsaved_changes": "未保存的更改",
            "confirm_close": "未保存的更改将丢失。确定关闭？",
            "confirm_reload": "未保存的更改将丢失。继续？",
            "confirm_delete": "确定删除？",
            "select_node": "请选择一个节点！",
            "select_item": "请选择一个项目！",
            "key_prompt": "键/名称：",
            "type_prompt": "类型 (string/number/boolean/object/array)：",
            "value_prompt": "值：",
            "search_prompt": "搜索词：",
            "template_prompt": "模板名称：",
            "edit_prompt": "当前值：{}\n新值：",
            "context_add": "➕ 添加",
            "context_edit": "✏️ 编辑",
            "context_delete": "🗑️ 删除",
            "context_copy": "📋 复制到编辑器",
            "context_scroll": "🎯 滚动到此点",
            "object_edit_info": "对象和数组只能通过原始编辑器编辑。",
            "tree_key": "键 / 属性",
            "tree_type": "类型",
            "tree_value": "值"
        }
    
    def get_japanese_translations(self):
        return {
            "title": "JSON エディタ",
            "structure": "📁 JSON 構造",
            "raw_editor": "📝 生JSONエディタ",
            "templates": "🚀 クイックテンプレート",
            "add": "➕ 追加",
            "edit": "✏️ 編集",
            "delete": "🗑️ 削除",
            "search": "🔍 検索",
            "save": "💾 保存",
            "reload": "🔄 再読み込み",
            "validate": "✅ 検証",
            "format": "🧹 フォーマット",
            "ready": "✅ 準備完了",
            "modified": "✏️ 変更済み",
            "saved": "✅ 保存済み",
            "project_spec": "📋 プロジェクト仕様",
            "api_design": "🔌 API設計",
            "test_cases": "🧪 テストケース",
            "config": "⚙️ 設定",
            "data_model": "📊 データモデル",
            "settings": "⚙️ 設定",
            "dark_mode": "🌙 ダークモード",
            "language": "🌐 言語",
            "file_not_found": "ファイルが見つかりません",
            "syntax_error": "JSON構文エラー",
            "save_success": "ファイルの保存に成功しました！",
            "validation_ok": "✅ JSONは構文的に正しいです！",
            "validation_error": "❌ JSONエラー",
            "unsaved_changes": "未保存の変更",
            "confirm_close": "未保存の変更は失われます。本当に閉じますか？",
            "confirm_reload": "未保存の変更は失われます。続行しますか？",
            "confirm_delete": "本当に削除しますか？",
            "select_node": "ノードを選択してください！",
            "select_item": "項目を選択してください！",
            "key_prompt": "キー/名前：",
            "type_prompt": "タイプ (string/number/boolean/object/array)：",
            "value_prompt": "値：",
            "search_prompt": "検索語：",
            "template_prompt": "テンプレート名：",
            "edit_prompt": "現在の値：{}\n新しい値：",
            "context_add": "➕ 追加",
            "context_edit": "✏️ 編集",
            "context_delete": "🗑️ 削除",
            "context_copy": "📋 エディタにコピー",
            "context_scroll": "🎯 このポイントにスクロール",
            "object_edit_info": "オブジェクトと配列はRawエディタでのみ編集できます。",
            "tree_key": "キー / プロパティ",
            "tree_type": "タイプ",
            "tree_value": "値"
        }
    
    def get_korean_translations(self):
        return {
            "title": "JSON 편집기",
            "structure": "📁 JSON 구조",
            "raw_editor": "📝 원본 JSON 편집기",
            "templates": "🚀 빠른 템플릿",
            "add": "➕ 추가",
            "edit": "✏️ 편집",
            "delete": "🗑️ 삭제",
            "search": "🔍 검색",
            "save": "💾 저장",
            "reload": "🔄 다시 로드",
            "validate": "✅ 검증",
            "format": "🧹 포맷",
            "ready": "✅ 준비됨",
            "modified": "✏️ 수정됨",
            "saved": "✅ 저장됨",
            "project_spec": "📋 프로젝트 사양",
            "api_design": "🔌 API 설계",
            "test_cases": "🧪 테스트 케이스",
            "config": "⚙️ 설정",
            "data_model": "📊 데이터 모델",
            "settings": "⚙️ 설정",
            "dark_mode": "🌙 다크 모드",
            "language": "🌐 언어",
            "file_not_found": "파일을 찾을 수 없습니다",
            "syntax_error": "JSON 구문 오류",
            "save_success": "파일이 성공적으로 저장되었습니다!",
            "validation_ok": "✅ JSON이 구문적으로 올바릅니다!",
            "validation_error": "❌ JSON 오류",
            "unsaved_changes": "저장되지 않은 변경 사항",
            "confirm_close": "저장되지 않은 변경 사항이 손실됩니다. 정말 닫으시겠습니까?",
            "confirm_reload": "저장되지 않은 변경 사항이 손실됩니다. 계속하시겠습니까?",
            "confirm_delete": "정말 삭제하시겠습니까?",
            "select_node": "노드를 선택해 주세요!",
            "select_item": "항목을 선택해 주세요!",
            "key_prompt": "키/이름:",
            "type_prompt": "유형 (string/number/boolean/object/array):",
            "value_prompt": "값:",
            "search_prompt": "검색어:",
            "template_prompt": "템플릿 이름:",
            "edit_prompt": "현재 값: {}\n새 값:",
            "context_add": "➕ 추가",
            "context_edit": "✏️ 편집",
            "context_delete": "🗑️ 삭제",
            "context_copy": "📋 편집기에 복사",
            "context_scroll": "🎯 이 지점으로 스크롤",
            "object_edit_info": "객체와 배열은 Raw 편집기를 통해서만 편집할 수 있습니다.",
            "tree_key": "키 / 속성",
            "tree_type": "유형",
            "tree_value": "값"
        }
    
    def t(self, key):
        """Get translation for current language"""
        return self.translations[self.language].get(key, key)
    
    def load_json(self):
        if not os.path.exists(self.filename):
            messagebox.showerror(self.t("file_not_found"), f"{self.t('file_not_found')}: '{self.filename}'")
            return False
            
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                self.data = json.loads(content)
            print(f"✅ JSON file '{self.filename}' loaded successfully!")
            self.modified = False
            return True
        except json.JSONDecodeError as e:
            error_msg = f"{self.t('syntax_error')}:\n{e}\n\n"
            error_msg += f"Position: Line {e.lineno}, Column {e.colno}\n"
            
            lines = content.split('\n')
            if e.lineno <= len(lines):
                error_msg += f"Error line:\n{lines[e.lineno-1]}\n"
                error_msg += " " * (e.colno - 1) + "^\n"
            
            messagebox.showerror(self.t("syntax_error"), error_msg)
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Loading error: {e}")
            return False
    
    def setup_gui(self):
        self.root = tk.Tk()
        self.update_title()
        self.root.geometry("1600x1000")
        
        # Bind close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Haupt-Frame mit PanedWindow für bessere Größenanpassung
        main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Linke Seite: Baumansicht (50%)
        left_frame = ttk.Frame(main_paned)
        main_paned.add(left_frame, weight=1)
        
        # Rechte Seite: Raw Editor (50%)
        right_frame = ttk.Frame(main_paned)
        main_paned.add(right_frame, weight=1)
        
        # === LINKE SEITE: STRUKTUR-ANSICHT ===
        tree_frame = ttk.LabelFrame(left_frame, text=self.t("structure"))
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=(0,5))
        
        # Edit-Buttons über dem Baum
        edit_button_frame = ttk.Frame(tree_frame)
        edit_button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(edit_button_frame, text=self.t("add"), 
                  command=self.add_item, width=14).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text=self.t("edit"), 
                  command=self.edit_item, width=14).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text=self.t("delete"), 
                  command=self.delete_item, width=14).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text=self.t("search"), 
                  command=self.search_dialog, width=14).pack(side=tk.LEFT, padx=2)
        
        # Baum mit besserem Styling
        tree_container = ttk.Frame(tree_frame)
        tree_container.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(tree_container, columns=('type', 'value'), show='tree headings', height=25)
        self.tree.heading('#0', text=self.t("tree_key"))
        self.tree.heading('type', text=self.t("tree_type"))
        self.tree.heading('value', text=self.t("tree_value"))
        
        # Spaltenbreiten anpassen
        self.tree.column('#0', width=300, minwidth=200)
        self.tree.column('type', width=100, minwidth=80)
        self.tree.column('value', width=400, minwidth=200)
        
        # Scrollbars für Baum
        vsb = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(tree_container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Tags für verschiedene Ebenen mit Farben
        self.setup_tree_tags()
        
        # Bind events
        self.tree.bind('<Double-1>', self.toggle_node)
        self.tree.bind('<Button-3>', self.show_context_menu)
        
        # === RECHTE SEITE: RAW EDITOR ===
        raw_frame = ttk.LabelFrame(right_frame, text=self.t("raw_editor"))
        raw_frame.pack(fill=tk.BOTH, expand=True, padx=(5,0))
        
        # Control Buttons über Raw Editor
        raw_control_frame = ttk.Frame(raw_frame)
        raw_control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(raw_control_frame, text=self.t("save"), 
                  command=self.save_json, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(raw_control_frame, text=self.t("reload"), 
                  command=self.reload_json, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(raw_control_frame, text=self.t("validate"), 
                  command=self.validate_json, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(raw_control_frame, text=self.t("format"), 
                  command=self.format_json, width=12).pack(side=tk.LEFT, padx=2)
        
        self.raw_text = scrolledtext.ScrolledText(raw_frame, wrap=tk.NONE, font=('Consolas', 10))
        self.raw_text.pack(fill=tk.BOTH, expand=True)
        self.raw_text.insert(tk.END, json.dumps(self.data, indent=2, ensure_ascii=False))
        self.raw_text.bind('<KeyRelease>', self.on_raw_edit)
        
        # === UNTERE LEISTE: TEMPLATES & EINSTELLUNGEN ===
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=(0,10))
        
        # Template Buttons
        template_frame = ttk.LabelFrame(bottom_frame, text=self.t("templates"))
        template_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10))
        
        template_buttons = [
            (self.t("project_spec"), "projekt_spec"),
            (self.t("api_design"), "api_design"),
            (self.t("test_cases"), "test_cases"),
            (self.t("config"), "config"),
            (self.t("data_model"), "datenmodell")
        ]
        
        for text, template_type in template_buttons:
            ttk.Button(template_frame, text=text, 
                      command=lambda t=template_type: self.add_template(t),
                      width=15).pack(side=tk.LEFT, padx=2, pady=2)
        
        # Settings Buttons
        settings_frame = ttk.LabelFrame(bottom_frame, text=self.t("settings"))
        settings_frame.pack(side=tk.RIGHT)
        
        # Dark Mode Toggle
        self.dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        ttk.Checkbutton(settings_frame, text=self.t("dark_mode"), 
                       variable=self.dark_mode_var,
                       command=self.toggle_dark_mode).pack(side=tk.LEFT, padx=5)
        
        # Language Selector
        lang_frame = ttk.Frame(settings_frame)
        lang_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(lang_frame, text=self.t("language") + ":").pack(side=tk.LEFT)
        
        self.lang_var = tk.StringVar(value=self.language)
        lang_combo = ttk.Combobox(lang_frame, textvariable=self.lang_var, 
                                 values=["de", "en", "es", "zh", "ja", "ko"],
                                 state="readonly", width=8)
        lang_combo.pack(side=tk.LEFT, padx=5)
        lang_combo.bind('<<ComboboxSelected>>', self.change_language)
        
        # Status Bar
        self.status_label = ttk.Label(settings_frame, text=self.t("ready"), foreground="green")
        self.status_label.pack(side=tk.LEFT, padx=(20,0))
        
        # Context Menu
        self.setup_context_menu()
        
        # Jetzt erst das Theme anwenden, nachdem alle Widgets erstellt sind
        self.apply_theme()
        
        self.populate_tree()
    
    def setup_tree_tags(self):
        """Setup tree tags for light/dark mode"""
        if self.dark_mode:
            # Dark mode colors
            self.tree.tag_configure('level_0', background='#2d2d2d', foreground='#ffffff')
            self.tree.tag_configure('level_1', background='#3d3d3d', foreground='#ffffff')
            self.tree.tag_configure('level_2', background='#4d4d4d', foreground='#ffffff')
            self.tree.tag_configure('level_3', background='#5d5d5d', foreground='#ffffff')
            self.tree.tag_configure('level_4', background='#6d6d6d', foreground='#ffffff')
            self.tree.tag_configure('object', foreground='#66ccff')
            self.tree.tag_configure('array', foreground='#ff9966')
            self.tree.tag_configure('value', foreground='#cccccc')
            self.tree.tag_configure('found', background='#555500')
        else:
            # Light mode colors
            self.tree.tag_configure('level_0', background='#f0f8ff')
            self.tree.tag_configure('level_1', background='#fff0f5')
            self.tree.tag_configure('level_2', background='#f0fff0')
            self.tree.tag_configure('level_3', background='#fff8dc')
            self.tree.tag_configure('level_4', background='#f5f5f5')
            self.tree.tag_configure('object', foreground='#0066cc')
            self.tree.tag_configure('array', foreground='#cc6600')
            self.tree.tag_configure('value', foreground='#333333')
            self.tree.tag_configure('found', background='yellow')
    
    def setup_context_menu(self):
        """Setup context menu with translations"""
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label=self.t("context_add"), command=self.add_item)
        self.context_menu.add_command(label=self.t("context_edit"), command=self.edit_item)
        self.context_menu.add_command(label=self.t("context_delete"), command=self.delete_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=self.t("context_copy"), command=self.copy_to_editor)
        self.context_menu.add_command(label=self.t("context_scroll"), command=self.scroll_to_item)
    
    def apply_theme(self):
        """Apply light/dark theme to the application"""
        if self.dark_mode:
            # Dark theme
            self.root.configure(background='#2d2d2d')
            style = ttk.Style()
            style.theme_use('clam')
            style.configure('.', background='#2d2d2d', foreground='white')
            style.configure('TLabel', background='#2d2d2d', foreground='white')
            style.configure('TFrame', background='#2d2d2d')
            style.configure('TLabelframe', background='#2d2d2d', foreground='white')
            style.configure('TLabelframe.Label', background='#2d2d2d', foreground='white')
            style.configure('TButton', background='#3d3d3d', foreground='white')
            style.configure('TEntry', fieldbackground='#3d3d3d', foreground='white')
            style.configure('TCombobox', fieldbackground='#3d3d3d', foreground='white')
            style.configure('Treeview', background='#2d2d2d', foreground='white', fieldbackground='#2d2d2d')
            style.map('Treeview', background=[('selected', '#0078d7')])
            
            # Raw Text Widget für Dark Mode
            if hasattr(self, 'raw_text'):
                self.raw_text.configure(background='#1e1e1e', foreground='#ffffff', 
                                      insertbackground='white')
        else:
            # Light theme
            self.root.configure(background='#f0f0f0')  # Linux-kompatible Farbe
            style = ttk.Style()
            style.theme_use('clam')
            style.configure('.', background='#f0f0f0', foreground='black')
            style.configure('TLabel', background='#f0f0f0', foreground='black')
            style.configure('TFrame', background='#f0f0f0')
            style.configure('TLabelframe', background='#f0f0f0', foreground='black')
            style.configure('TLabelframe.Label', background='#f0f0f0', foreground='black')
            style.configure('TButton', background='#e0e0e0', foreground='black')
            style.configure('TEntry', fieldbackground='white', foreground='black')
            style.configure('TCombobox', fieldbackground='white', foreground='black')
            style.configure('Treeview', background='white', foreground='black', fieldbackground='white')
            style.map('Treeview', background=[('selected', '#0078d7')])
            
            # Raw Text Widget für Light Mode
            if hasattr(self, 'raw_text'):
                self.raw_text.configure(background='white', foreground='black',
                                      insertbackground='black')
    
    def toggle_dark_mode(self):
        """Toggle dark mode on/off"""
        self.dark_mode = self.dark_mode_var.get()
        self.apply_theme()
        self.setup_tree_tags()
        self.refresh_views()
    
    def change_language(self, event=None):
        """Change application language"""
        self.language = self.lang_var.get()
        self.update_ui_texts()
        self.setup_context_menu()
    
    def update_ui_texts(self):
        """Update all UI texts with current language"""
        # Update title
        self.update_title()
        
        # Update tree headings
        self.tree.heading('#0', text=self.t("tree_key"))
        self.tree.heading('type', text=self.t("tree_type"))
        self.tree.heading('value', text=self.t("tree_value"))
        
        # Update all labels and buttons
        for widget in self.root.winfo_children():
            self.update_widget_texts(widget)
        
        # Update status
        if self.modified:
            self.status_label.config(text=self.t("modified"), foreground="orange")
        else:
            self.status_label.config(text=self.t("saved"), foreground="green")
    
    def update_widget_texts(self, widget):
        """Recursively update all widget texts"""
        try:
            if isinstance(widget, ttk.LabelFrame):
                widget.config(text=self.get_original_label(widget))
            elif isinstance(widget, ttk.Button):
                widget.config(text=self.get_original_button_text(widget))
            elif isinstance(widget, ttk.Label):
                widget.config(text=self.get_original_label_text(widget))
            
            # Rekursiv für Child-Widgets
            for child in widget.winfo_children():
                self.update_widget_texts(child)
        except:
            pass
    
    def get_original_label(self, widget):
        """Get original label text based on current translation"""
        # Diese Methode müsste erweitert werden um spezifische Widgets zu identifizieren
        # Für jetzt verwenden wir eine einfache Mapping-Logik
        original_text = str(widget.cget('text'))
        for key, translation in self.translations[self.language].items():
            if translation == original_text:
                return translation
        return original_text
    
    def get_original_button_text(self, widget):
        """Get original button text based on current translation"""
        original_text = str(widget.cget('text'))
        for key, translation in self.translations[self.language].items():
            if translation == original_text:
                return translation
        return original_text
    
    def get_original_label_text(self, widget):
        """Get original label text based on current translation"""
        original_text = str(widget.cget('text'))
        for key, translation in self.translations[self.language].items():
            if translation == original_text:
                return translation
        return original_text
    
    def update_title(self):
        """Update window title"""
        title = f"{self.t('title')} - {self.filename}"
        if self.modified:
            title += " *"
        self.root.title(title)
    
    def populate_tree(self, parent='', json_dict=None, level=0):
        if json_dict is None:
            json_dict = self.data
            root_node = self.tree.insert('', 'end', text=self.filename, 
                                       values=('📁 ROOT', ''), 
                                       tags=('level_0', 'object'), open=True)  # Nur Ebene 1 aufgeklappt
            parent = root_node
            level = 1
            
        for key, value in json_dict.items():
            tag = f'level_{min(level, 4)}'
            
            if isinstance(value, dict):
                # Nur Ebene 1 standardmäßig aufgeklappt
                node = self.tree.insert(parent, 'end', text=str(key), 
                                      values=('📁 OBJECT', f'{len(value)} items'),
                                      tags=(tag, 'object'), open=(level == 1))  # Nur Ebene 1 aufgeklappt
                self.populate_tree(node, value, level + 1)
            elif isinstance(value, list):
                node = self.tree.insert(parent, 'end', text=str(key), 
                                      values=('📋 ARRAY', f'{len(value)} items'),
                                      tags=(tag, 'array'), open=(level == 1))  # Nur Ebene 1 aufgeklappt
                for i, item in enumerate(value):
                    item_tag = f'level_{min(level + 1, 4)}'
                    if isinstance(item, (dict, list)):
                        item_type = '📁 OBJECT' if isinstance(item, dict) else '📋 ARRAY'
                        item_text = f"[{i}]"
                        sub_node = self.tree.insert(node, 'end', text=item_text,
                                                  values=(item_type, '...'),
                                                  tags=(item_tag, 'object' if isinstance(item, dict) else 'array'),
                                                  open=False)  # Ab Ebene 2 nicht aufgeklappt
                        self.populate_tree(sub_node, item if isinstance(item, dict) else {f"[{i}]": item}, level + 2)
                    else:
                        self.tree.insert(node, 'end', text=f"[{i}]", 
                                       values=('📄 VALUE', self.truncate_value(item)),
                                       tags=(item_tag, 'value'))
            else:
                value_type = '📄 STRING' if isinstance(value, str) else '🔢 NUMBER' if isinstance(value, (int, float)) else '⚡ BOOLEAN' if isinstance(value, bool) else '❓ OTHER'
                self.tree.insert(parent, 'end', text=str(key), 
                               values=(value_type, self.truncate_value(value)),
                               tags=(tag, 'value'))
    
    def truncate_value(self, value, max_length=60):
        str_value = str(value)
        if len(str_value) > max_length:
            return str_value[:max_length] + "..."
        return str_value
    
    def toggle_node(self, event):
        item = self.tree.selection()[0]
        self.tree.item(item, open=not self.tree.item(item, 'open'))
    
    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def copy_to_editor(self):
        item = self.tree.selection()
        if item:
            item_path = self.get_item_path(item[0])
            data = self.get_data_at_path(item_path)
            if data:
                self.raw_text.insert(tk.END, f"\n\n// {self.t('context_copy')}: {item_path}\n{json.dumps(data, indent=2, ensure_ascii=False)}")
                self.set_modified(True)
    
    def scroll_to_item(self):
        item = self.tree.selection()
        if item:
            self.tree.see(item[0])
    
    def add_template(self, template_type):
        templates = {
            "projekt_spec": {
                "project_basics": {
                    "name": "Project_Name",
                    "goal": "Short_Description",
                    "type": "Web_App/Mobile_App/Desktop_App",
                    "target_systems": ["linux", "windows", "macos"]
                }
            },
            "api_design": {
                "base_url": "https://api.example.com/v1",
                "endpoints": [
                    {
                        "path": "/users",
                        "method": "GET",
                        "description": "List_of_Users"
                    }
                ]
            },
            "test_cases": {
                "test_suite": "My_Test_Suite",
                "test_cases": [
                    {
                        "name": "Test_Case_1",
                        "description": "Test_Case_Description"
                    }
                ]
            },
            "config": {
                "app_name": "My_App",
                "version": "1.0.0",
                "settings": {
                    "debug": True,
                    "port": 3000
                }
            },
            "datenmodell": {
                "entities": [
                    {
                        "name": "User",
                        "attributes": {
                            "id": "UUID",
                            "email": "string"
                        }
                    }
                ]
            }
        }
        
        if template_type in templates:
            key_name = simpledialog.askstring(self.t("templates"), self.t("template_prompt"))
            if key_name:
                self.data[key_name] = templates[template_type]
                self.refresh_views()
                self.set_modified(True)
    
    def add_item(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Warning", self.t("select_node"))
            return
        
        parent_item = item[0]
        parent_path = self.get_item_path(parent_item)
        
        key = simpledialog.askstring(self.t("add"), self.t("key_prompt"))
        if not key:
            return
            
        value_type = simpledialog.askstring(self.t("add"), self.t("type_prompt"))
        if not value_type:
            return
        
        value = None
        if value_type == "string":
            value = simpledialog.askstring(self.t("add"), self.t("value_prompt"))
        elif value_type == "number":
            value = simpledialog.askfloat(self.t("add"), self.t("value_prompt"))
        elif value_type == "boolean":
            value = messagebox.askyesno(self.t("add"), self.t("value_prompt"))
        elif value_type in ["object", "array"]:
            value = {} if value_type == "object" else []
        
        if value is not None:
            target = self.get_data_at_path(parent_path)
            if isinstance(target, dict):
                target[key] = value
            elif isinstance(target, list):
                try:
                    index = int(key)
                    if 0 <= index <= len(target):
                        target.insert(index, value)
                    else:
                        target.append(value)
                except ValueError:
                    target.append(value)
            
            self.refresh_views()
            self.set_modified(True)
    
    def edit_item(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Warning", self.t("select_item"))
            return
        
        item_path = self.get_item_path(item[0])
        current_data = self.get_data_at_path(item_path)
        
        if isinstance(current_data, (dict, list)):
            messagebox.showinfo("Info", self.t("object_edit_info"))
            return
        
        new_value = simpledialog.askstring(self.t("edit"), self.t("edit_prompt").format(current_data))
        if new_value is not None:
            try:
                if isinstance(current_data, bool):
                    new_value = new_value.lower() in ['true', '1', 'yes', 'ja']
                elif isinstance(current_data, (int, float)):
                    new_value = float(new_value) if '.' in new_value else int(new_value)
            except ValueError:
                pass
            
            self.set_data_at_path(item_path, new_value)
            self.refresh_views()
            self.set_modified(True)
    
    def delete_item(self):
        item = self.tree.selection()
        if not item:
            return
        
        if messagebox.askyesno(self.t("delete"), self.t("confirm_delete")):
            item_path = self.get_item_path(item[0])
            parent_path = '/'.join(item_path.split('/')[:-1])
            key = item_path.split('/')[-1]
            
            parent_data = self.get_data_at_path(parent_path)
            if isinstance(parent_data, dict):
                del parent_data[key]
            elif isinstance(parent_data, list):
                try:
                    index = int(key.strip('[]'))
                    parent_data.pop(index)
                except (ValueError, IndexError):
                    pass
            
            self.refresh_views()
            self.set_modified(True)
    
    def search_dialog(self):
        search_term = simpledialog.askstring(self.t("search"), self.t("search_prompt"))
        if search_term:
            self.search_tree(search_term.lower())
    
    def search_tree(self, search_term):
        for item in self.tree.get_children():
            self.tree.item(item, tags=())
        
        for item in self.tree.get_children(''):
            self._search_in_children(item, search_term)
    
    def _search_in_children(self, parent, search_term):
        for child in self.tree.get_children(parent):
            text = self.tree.item(child, 'text').lower()
            values = self.tree.item(child, 'values')
            value_str = ' '.join(str(v) for v in values).lower()
            
            if search_term in text or search_term in value_str:
                self.tree.item(child, tags=('found',))
                self._expand_parents(child)
            
            self._search_in_children(child, search_term)
    
    def _expand_parents(self, item):
        parent = self.tree.parent(item)
        if parent:
            self.tree.item(parent, open=True)
            self._expand_parents(parent)
    
    def get_item_path(self, item):
        path = []
        while item:
            path.append(self.tree.item(item, 'text'))
            item = self.tree.parent(item)
        return '/'.join(reversed(path))
    
    def get_data_at_path(self, path):
        if path == self.filename:
            return self.data
        
        keys = path.replace(self.filename + '/', '').split('/')
        current = self.data
        
        for key in keys:
            if key.startswith('[') and key.endswith(']'):
                try:
                    index = int(key[1:-1])
                    current = current[index]
                except (ValueError, IndexError):
                    return None
            else:
                current = current.get(key, None)
                if current is None:
                    return None
        return current
    
    def set_data_at_path(self, path, value):
        keys = path.replace(self.filename + '/', '').split('/')
        current = self.data
        
        for key in keys[:-1]:
            if key.startswith('[') and key.endswith(']'):
                index = int(key[1:-1])
                current = current[index]
            else:
                current = current[key]
        
        last_key = keys[-1]
        if last_key.startswith('[') and last_key.endswith(']'):
            index = int(last_key[1:-1])
            current[index] = value
        else:
            current[last_key] = value
    
    def refresh_views(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_tree()
        
        self.raw_text.delete(1.0, tk.END)
        self.raw_text.insert(tk.END, json.dumps(self.data, indent=2, ensure_ascii=False))
    
    def set_modified(self, modified):
        self.modified = modified
        self.update_title()
        if modified:
            self.status_label.config(text=self.t("modified"), foreground="orange")
        else:
            self.status_label.config(text=self.t("saved"), foreground="green")
    
    def on_raw_edit(self, event):
        self.set_modified(True)
    
    def save_json(self):
        try:
            new_content = self.raw_text.get(1.0, tk.END).strip()
            json.loads(new_content)
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            self.load_json()
            self.refresh_views()
            self.set_modified(False)
            messagebox.showinfo(self.t("save"), self.t("save_success"))
            
        except json.JSONDecodeError as e:
            messagebox.showerror(self.t("syntax_error"), f"{self.t('validation_error')}: {e}")
    
    def reload_json(self):
        if self.modified:
            if not messagebox.askyesno(self.t("unsaved_changes"), self.t("confirm_reload")):
                return
        
        if self.load_json():
            self.refresh_views()
    
    def validate_json(self):
        try:
            json.loads(self.raw_text.get(1.0, tk.END))
            messagebox.showinfo(self.t("validate"), self.t("validation_ok"))
        except json.JSONDecodeError as e:
            messagebox.showerror(self.t("validation_error"), f"{self.t('validation_error')}: {e}")
    
    def format_json(self):
        try:
            content = self.raw_text.get(1.0, tk.END)
            parsed = json.loads(content)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
            self.raw_text.delete(1.0, tk.END)
            self.raw_text.insert(tk.END, formatted)
            self.set_modified(True)
        except json.JSONDecodeError as e:
            messagebox.showerror(self.t("format"), f"{self.t('validation_error')}: {e}")
    
    def on_closing(self):
        if self.modified:
            if messagebox.askyesno(self.t("unsaved_changes"), self.t("confirm_close")):
                self.root.destroy()
        else:
            self.root.destroy()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        json_files = [f for f in os.listdir('.') if f.endswith('.json')]
        if json_files:
            filename = json_files[0]
            print(f"Using file: {filename}")
        else:
            print("No JSON files found!")
            sys.exit(1)
    
    viewer = JSONViewer(filename)
    viewer.root.mainloop()
