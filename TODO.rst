* Add an explicit check to see if the keyfile passed to the checker works before identifying the need for a password prompt
* Move console to console_pretty and make a console_plain that JUST outputs issues to stdout (for piping)
* Wrap kppy exceptions up for uniform client access