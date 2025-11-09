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
        if self.load_json():
            self.setup_gui()
    
    def load_json(self):
        if not os.path.exists(self.filename):
            messagebox.showerror("Fehler", f"Datei '{self.filename}' nicht gefunden!")
            return False
            
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                self.data = json.loads(content)
            print(f"✅ JSON-Datei '{self.filename}' erfolgreich geladen!")
            self.modified = False
            return True
        except json.JSONDecodeError as e:
            error_msg = f"JSON Syntax Fehler:\n{e}\n\n"
            error_msg += f"Position: Zeile {e.lineno}, Spalte {e.colno}\n"
            
            lines = content.split('\n')
            if e.lineno <= len(lines):
                error_msg += f"Fehlerhafte Zeile:\n{lines[e.lineno-1]}\n"
                error_msg += " " * (e.colno - 1) + "^\n"
            
            messagebox.showerror("JSON Syntax Fehler", error_msg)
            return False
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden: {e}")
            return False
    
    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title(f"JSON Editor - {self.filename}" + (" *" if self.modified else ""))
        self.root.geometry("1400x900")
        
        # Bind close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Haupt-Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Linke Seite: Baumansicht mit Edit-Buttons
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tree_frame = ttk.LabelFrame(left_frame, text="Struktur-Ansicht")
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Edit-Buttons über dem Baum
        edit_button_frame = ttk.Frame(tree_frame)
        edit_button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(edit_button_frame, text="➕ Hinzufügen", 
                  command=self.add_item, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text="✏️ Bearbeiten", 
                  command=self.edit_item, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text="🗑️ Löschen", 
                  command=self.delete_item, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(edit_button_frame, text="🔍 Suchen", 
                  command=self.search_dialog, width=12).pack(side=tk.LEFT, padx=2)
        
        self.tree = ttk.Treeview(tree_frame, columns=('value',), show='tree headings')
        self.tree.heading('#0', text='Key / Property')
        self.tree.heading('value', text='Value / Type')
        
        # Scrollbars für Baum
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind events
        self.tree.bind('<Double-1>', self.toggle_node)
        self.tree.bind('<Button-3>', self.show_context_menu)  # Right-click
        
        # Rechte Seite: Raw Editor
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10,0))
        
        raw_frame = ttk.LabelFrame(right_frame, text="Raw JSON Editor")
        raw_frame.pack(fill=tk.BOTH, expand=True)
        
        self.raw_text = scrolledtext.ScrolledText(raw_frame, height=20, wrap=tk.NONE)
        self.raw_text.pack(fill=tk.BOTH, expand=True)
        self.raw_text.insert(tk.END, json.dumps(self.data, indent=2, ensure_ascii=False))
        self.raw_text.bind('<KeyRelease>', self.on_raw_edit)
        
        # Control Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10,0))
        
        ttk.Button(button_frame, text="💾 Speichern", 
                  command=self.save_json).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(button_frame, text="🔄 Neu laden", 
                  command=self.reload_json).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(button_frame, text="✅ Validieren", 
                  command=self.validate_json).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(button_frame, text="🧹 Formatieren", 
                  command=self.format_json).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(button_frame, text="➕ Neue Anforderung", 
                  command=self.add_requirement_template).pack(side=tk.LEFT, padx=(0,5))
        
        # Status Bar
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(5,0))
        
        self.status_label = ttk.Label(status_frame, text="Bereit")
        self.status_label.pack(side=tk.LEFT)
        
        # Context Menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Hinzufügen", command=self.add_item)
        self.context_menu.add_command(label="Bearbeiten", command=self.edit_item)
        self.context_menu.add_command(label="Löschen", command=self.delete_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="In Raw-Editor zeigen", command=self.show_in_raw)
        
        self.populate_tree()
    
    def populate_tree(self, parent='', json_dict=None):
        if json_dict is None:
            json_dict = self.data
            root_node = self.tree.insert('', 'end', text=self.filename, 
                                       values=('📁 Root Object',), open=True)
            parent = root_node
            
        for key, value in json_dict.items():
            if isinstance(value, dict):
                node = self.tree.insert(parent, 'end', text=str(key), 
                                      values=('📁 Object',), tags=('object',))
                self.populate_tree(node, value)
            elif isinstance(value, list):
                node = self.tree.insert(parent, 'end', text=str(key), 
                                      values=(f'📋 Array [{len(value)} items]',), tags=('array',))
                for i, item in enumerate(value):
                    if isinstance(item, (dict, list)):
                        self.populate_tree(node, {f"[{i}]": item})
                    else:
                        self.tree.insert(node, 'end', text=f"[{i}]", 
                                       values=(f"📄 {self.truncate_value(item)}",), tags=('value',))
            else:
                self.tree.insert(parent, 'end', text=str(key), 
                               values=(f"📄 {self.truncate_value(value)}",), tags=('value',))
    
    def truncate_value(self, value, max_length=50):
        str_value = str(value)
        return str_value[:max_length] + "..." if len(str_value) > max_length else str_value
    
    def toggle_node(self, event):
        item = self.tree.selection()[0]
        self.tree.item(item, open=not self.tree.item(item, 'open'))
    
    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def add_item(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Warnung", "Bitte wählen Sie einen Knoten aus!")
            return
        
        parent_item = item[0]
        parent_path = self.get_item_path(parent_item)
        
        # Dialog für neuen Eintrag
        key = simpledialog.askstring("Hinzufügen", "Schlüssel/Name:")
        if not key:
            return
            
        value_type = simpledialog.askstring("Typ wählen", "Typ (string/number/boolean/object/array):")
        if not value_type:
            return
        
        value = None
        if value_type == "string":
            value = simpledialog.askstring("Wert", "String Wert:")
        elif value_type == "number":
            value = simpledialog.askfloat("Wert", "Numerischer Wert:")
        elif value_type == "boolean":
            value = messagebox.askyesno("Wert", "Boolean Wert (Ja=True, Nein=False):")
        elif value_type in ["object", "array"]:
            value = {} if value_type == "object" else []
        
        if value is not None:
            # Füge zum Datenmodell hinzu
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
            messagebox.showwarning("Warnung", "Bitte wählen Sie einen Eintrag aus!")
            return
        
        item_path = self.get_item_path(item[0])
        current_data = self.get_data_at_path(item_path)
        
        if isinstance(current_data, (dict, list)):
            messagebox.showinfo("Info", "Objekte und Arrays können nur über Raw-Editor bearbeitet werden.")
            return
        
        new_value = simpledialog.askstring("Bearbeiten", f"Aktueller Wert: {current_data}\nNeuer Wert:")
        if new_value is not None:
            # Versuche Typ-Conversion
            try:
                if isinstance(current_data, bool):
                    new_value = new_value.lower() in ['true', '1', 'yes', 'ja']
                elif isinstance(current_data, (int, float)):
                    new_value = float(new_value) if '.' in new_value else int(new_value)
            except ValueError:
                pass  # Behalte als String
            
            self.set_data_at_path(item_path, new_value)
            self.refresh_views()
            self.set_modified(True)
    
    def delete_item(self):
        item = self.tree.selection()
        if not item:
            return
        
        if messagebox.askyesno("Löschen", "Wirklich löschen?"):
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
        search_term = simpledialog.askstring("Suchen", "Suchbegriff:")
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
    
    def show_in_raw(self):
        item = self.tree.selection()
        if item:
            # Scroll zum entsprechenden Teil im Raw-Editor
            self.status_label.config(text="Feature: In Raw-Editor zeigen")
    
    def add_requirement_template(self):
        templates = {
            "neue_funktion": {
                "name": "Neue_Funktion",
                "beschreibung": "Beschreibung_der_Neuen_Funktion",
                "anforderungen": [
                    "Anforderung_1",
                    "Anforderung_2"
                ],
                "implementierung": "noch_nicht_begonnen"
            },
            "hardware_komponente": {
                "name": "Neue_Hardware",
                "typ": "Sensor/Aktor",
                "schnittstelle": "USB/SPI/I2C",
                "konfiguration": {
                    "parameter": "wert"
                }
            },
            "test_case": {
                "name": "Neuer_Test",
                "beschreibung": "Testbeschreibung",
                "erwartetes_ergebnis": "Erwartetes_Verhalten",
                "status": "nicht_getestet"
            }
        }
        
        template_choice = simpledialog.askstring("Template", "Template wählen (neue_funktion/hardware_komponente/test_case):")
        if template_choice in templates:
            # Füge zum Root hinzu oder an spezifischer Stelle
            key_name = simpledialog.askstring("Schlüssel", "Name für neuen Eintrag:")
            if key_name:
                self.data[key_name] = templates[template_choice]
                self.refresh_views()
                self.set_modified(True)
    
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
                # Array index
                try:
                    index = int(key[1:-1])
                    current = current[index]
                except (ValueError, IndexError):
                    return None
            else:
                # Object key
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
        # Aktualisiere Baum
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_tree()
        
        # Aktualisiere Raw-Editor
        self.raw_text.delete(1.0, tk.END)
        self.raw_text.insert(tk.END, json.dumps(self.data, indent=2, ensure_ascii=False))
    
    def set_modified(self, modified):
        self.modified = modified
        title = f"JSON Editor - {self.filename}"
        if modified:
            title += " *"
        self.root.title(title)
        self.status_label.config(text="Geändert" if modified else "Gespeichert")
    
    def on_raw_edit(self, event):
        self.set_modified(True)
    
    def save_json(self):
        try:
            new_content = self.raw_text.get(1.0, tk.END).strip()
            # Validieren
            json.loads(new_content)
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # Reload to update data model
            self.load_json()
            self.refresh_views()
            self.set_modified(False)
            messagebox.showinfo("Erfolg", "Datei erfolgreich gespeichert!")
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Syntax Fehler", f"Ungültiges JSON: {e}")
    
    def reload_json(self):
        if self.modified:
            if not messagebox.askyesno("Ungespeicherte Änderungen", "Ungespeicherte Änderungen gehen verloren. Fortfahren?"):
                return
        
        if self.load_json():
            self.refresh_views()
    
    def validate_json(self):
        try:
            json.loads(self.raw_text.get(1.0, tk.END))
            messagebox.showinfo("Validierung", "✅ JSON ist syntaktisch korrekt!")
        except json.JSONDecodeError as e:
            messagebox.showerror("Validierung", f"❌ JSON Fehler: {e}")
    
    def format_json(self):
        try:
            content = self.raw_text.get(1.0, tk.END)
            parsed = json.loads(content)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
            self.raw_text.delete(1.0, tk.END)
            self.raw_text.insert(tk.END, formatted)
            self.set_modified(True)
        except json.JSONDecodeError as e:
            messagebox.showerror("Formatieren", f"Kann nicht formatieren: {e}")
    
    def on_closing(self):
        if self.modified:
            if messagebox.askyesno("Ungespeicherte Änderungen", "Ungespeicherte Änderungen gehen verloren. Wirklich schließen?"):
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
            print(f"Verwende Datei: {filename}")
        else:
            print("Keine JSON-Dateien gefunden!")
            sys.exit(1)
    
    viewer = JSONViewer(filename)
    viewer.root.mainloop()
