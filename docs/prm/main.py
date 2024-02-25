from pathlib import Path

from js import ace, document
from pyodide.ffi.wrappers import add_event_listener

from main import validate_readme  # type: ignore[attr-defined]

editor_input = ace.edit("editor-input")
editor_input.setOption("maxLines", float("inf"))
editor_output = ace.edit("editor-output")
editor_output.setOption("maxLines", float("inf"))
editor_output.setReadOnly(True)


def on_keyup_editor_input(_: None) -> None:
    input_ = editor_input.getValue()
    output = validate_readme(input_.encode("utf-8"))
    if output is None:
        editor_output.setValue("No issues!")
    else:
        editor_output.setValue(output)


async def on_change_file_input(e) -> None:  # type: ignore[no-untyped-def] # noqa: ANN001
    file_list = e.target.files
    first_item = file_list.item(0)
    editor_input.setValue(await first_item.text())
    on_keyup_editor_input(None)


def main() -> None:
    with Path("README").open() as file:
        editor_input.setValue(file.read())
    on_keyup_editor_input(None)
    add_event_listener(
        document.getElementById("editor-input"),
        "keyup",
        on_keyup_editor_input,
    )
    add_event_listener(
        document.getElementById("file-input"),
        "change",
        on_change_file_input,
    )


if __name__ == "__main__":
    main()
