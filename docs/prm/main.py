import io
from pathlib import Path

from js import document
from pyodide.ffi.wrappers import add_event_listener

from main import validate_readme


def on_keyup_input_textarea(_: None) -> None:
    document.getElementById("input-textarea").style.height = "1px"
    document.getElementById(
        "input-textarea",
    ).style.height = f'{document.getElementById("input-textarea").scrollHeight}px'
    input_ = document.getElementById("input-textarea").value
    reader = io.BufferedReader(io.BytesIO(input_.encode("utf-8")))  # type: ignore[arg-type]
    wrapper = io.TextIOWrapper(reader)
    try:
        validate_readme(wrapper)
        document.getElementById("output-pre").innerHTML = "Correct!"
    except Exception as exception:  # noqa: BLE001
        document.getElementById("output-pre").innerHTML = exception


async def on_change_file_input(e) -> None:
    file_list = e.target.files
    first_item = file_list.item(0)
    document.getElementById("input-textarea").value = await first_item.text()
    on_keyup_input_textarea(None)


def main() -> None:
    with Path("README").open() as file:
        document.getElementById("input-textarea").value = file.read()
    on_keyup_input_textarea(None)
    add_event_listener(
        document.getElementById("input-textarea"),
        "keyup",
        on_keyup_input_textarea,
    )
    add_event_listener(
        document.getElementById("file-input"),
        "change",
        on_change_file_input,
    )


if __name__ == "__main__":
    main()
