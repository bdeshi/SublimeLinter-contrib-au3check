SublimeLinter-contrib-au3check
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [au3check][au] - the official AutoIt3 syntax checker utility. It will be used with files that have the “__autoit__” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `au3check` is installed on your system. To install `au3check`, do the following:
* Install [AutoIt3][au] - installation package includes `au3check.exe`.

**Note:** This plugin requires `au3check` 3.0.0 or later.

### Linter configuration
In order for `au3check` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further,
please read and follow the steps in [“Finding a linter executable”][finding-linter-exec] through “Validating your PATH” in the documentation.<br>
For example, if AutoIt is located at `C:\\programs\\Autoit`, your SublimeLinter user settings' `paths` entry might look like this:
```json
{
    "paths": {
        "windows": [
          "C:\\other\\linter\\paths\\",
          "C:\\programs\\autoit\\"
        ]
    }
}
```

Once you have installed and configured `au3check`, you can proceed to install the SublimeLinter-contrib-au3check plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `au3check`. Among the entries you should see `SublimeLinter-contrib-au3check`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings].<br>
SublimeLinter-contrib-au3check does not yet provide its own settings.

## Notes
This linter does not work with unsaved files. Save file or unsaved changes in it before invoking the linter.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.
5. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[au]: https://www.autoitscript.com/site/autoit/downloads/
[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[finding-linter-exec]: http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
