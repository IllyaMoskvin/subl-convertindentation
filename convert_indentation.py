import sublime, sublime_plugin

class ConvertIndentationCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        global_settings = sublime.load_settings('Preferences.sublime-settings')

        gtab_size = global_settings.get('tab_size')
        gtranslate_to_spaces = global_settings.get('translate_tabs_to_spaces')

        print("Point A")
        return

        # Now detect the indentation.
        self.view.run_command('detect_indentation')

        # Get the detected indentation for this view.
        vtranslate_to_spaces = self.view.settings().get('translate_tabs_to_spaces')
        vtab_size = self.view.settings().get('tab_size')

        print("Point B")

        if gtranslate_to_spaces == False:
            self.view.run_command('unexpand_tabs')
            self.view.settings().set('tab_size', gtab_size)
            return

        # If any of them are not equal, change it up.
        if (vtranslate_to_spaces == True and vtab_size != gtab_size):
            print("Converting Indentation")
            self.view.run_command('unexpand_tabs')
            self.view.settings().set('tab_size', gtab_size)
            self.view.run_command('expand_tabs')
            self.view.settings().set('translate_tabs_to_spaces', True)

        sublime.status_message('Automatically updated indentation for document')

class ConvertIndentionOnOpen(sublime_plugin.EventListener):
    def on_load(self, view):
        settings = sublime.load_settings('Convert Indentation.sublime-settings')
        if settings.get('convert_on_open', True):
            view.run_command('convert_indentation')
