# PyQt Figma Designer

## Overview

PyQt Figma Designer is a powerful tool designed to streamline the process of converting Figma files into PyQt6 code,
enabling the rapid development of professional graphical user interfaces (GUIs). Leveraging the Figma API, this project
offers a comprehensive solution for creating GUIs with PyQt6, using high-quality SVG components.

![GUI Screenshot](images/screenshot_gui_v4_1.png)

## Installation

Follow these steps to install PyQt Figma Designer on your system:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rombirli/PyQT-Figma-Designer.git
   cd PyQt-Figma-Designer
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a personal access token for Figma by following the
   instructions [here](https://www.figma.com/developers/api#access-tokens).

## Usage

### Graphical User Interface (GUI)

1. Launch the GUI with the following command:

   ```bash
   python pyqtfd-gui.py
   ```

2. In the "Create project" tab input the path to an empty directory where the project will be created.
   ![GUI Screenshot](images/screenshot_gui_v4_0.png)

3. Switch to the "Download" tab, input your Figma personal access token
   ![GUI Screenshot](images/screenshot_gui_v4_1.png)

4. Switch to the "Compile" tab and click the "Compile" button to generate the PyQt6 code.
   ![GUI Screenshot](images/screenshot_gui_v4_2.png)

6. Switch to the "Run" tab and click the "Run" button to run the generated GUI.
   ![GUI Screenshot](images/screenshot_gui_v4_3.png)

### Command Line Interface (CLI)

#### Creating new project

```bash
python pyqtfd-create.py -h
```

This command allows you to create a new PyQt-Figma-Designer project. It accepts the following options:

- `-p PATH, --project PATH`: Specifies the project directory where the generated files will be stored.
- `-c, --clear`: (Optional) Clears the project directory before generating the project.

Example usage:

```bash
python pyqtfd-create.py -p <project_directory> -c
```

#### Downloading Figma Files

```bash
python pyqtfd-download.py -h
```

This command allows you to download a Figma file as well as its images. It accepts the following options:

- `-p PATH, --project PATH`: Specifies the project directory where the generated files will be stored.
- `url URL, --url URL`: Specifies the Figma file URL.
- `-t TOKEN, --token TOKEN`: Specifies the Figma personal access token.
- `-ni, --no-images`: (Optional) When specified, images are not downloaded.

Example usage:

```bash
python pyqtfd-download.py -p <project_directory> -t <Figma_token> -url <Figma_URL>
```

#### Compiling PyQt-Figma-Designer Projects

```bash
python pyqtfd-compile.py -h
```

This command allows you to compile a PyQt-Figma-Designer project into a Python project. It accepts the following
options:

- `-p PATH, --project PATH`: Specifies the project directory where the PyQt-Figma-Designer project is located.
- `-s SCALE, --scale SCALE`: (Optional) Specifies the scale for the Figma components.
- `-ts TEXT_SCALE, --text-scale TEXT_SCALE`: (Optional) Specifies the scale for the Figma text components.
- `-owh, --overwrite-handler`: (Optional) When specified the `gui_handler.py` file is
  overwritten.
- `-owc, --overwrite-config`: (Optional) When specified the `components_config.py` file is
  overwritten.
- `-ows, --overwrite-strings`: (Optional) When specified the `strings.py` file is
  overwritten.

Example usage:

```bash
python pyqtfd-compile.py -p <project_directory> -s <scale>
```

These CLI commands provide flexibility and automation for working with PyQt Figma Designer, allowing you to efficiently
download Figma files and compile them into Python projects. For additional details on these commands, refer to the
provided help information.

### Generated Files

#### GUI

The main GUI file, `gui.py`, is generated in the output directory. Avoid editing this file, as it will be overwritten
during recompilation. Run this file to launch the generated GUI.

#### GUI Handler

The `gui_handler.py` file, also generated in the output directory, contains a class hierarchy that mirrors the Figma
file's structure. You can extend and customize these classes as needed, but be cautious not to overwrite them during
recompilation.

#### GUI Controller

Similarly, the `gui_controller.py` file in the output directory contains a class hierarchy representing the Figma file's
structure. Your code should call functions within these classes to update the GUI. Avoid editing this file to prevent
overwriting during recompilation.

#### Strings

The `strings.py` file in the output directory contains all the strings used in the GUI. You can edit this file to
translate it into another language, but be cautious not to overwrite it during recompilation.

#### Components Config

The `components_config.py` file in the output directory contains the configuration for the components. You can edit this
file to change the default values of the components, as well as their color, but be cautious not to overwrite it during
recompilation.

#### Figma Files

The downloaded Figma file is saved in the output directory as `figma_file.pickle`. Additionally, project images are
stored in the `images` subdirectory in png format.

#### SVG Files

SVG files are generated during compilation and can be found in the `svg` subdirectory. These SVG files are crucial for
displaying each GUI component.

## Supported Components

PyQt Figma Designer supports various components, each with specific naming conventions and hierarchies. To ensure proper
functionality, follow these guidelines:

### Components pack

For a quick components overview, you can access the Component
Pack [here](https://www.figma.com/file/AZD7bWnCwce9uAuTqa6aY5/Untitled?type=design&node-id=0%3A1&mode=design&t=0jee9KtQMinbOkMd-1)
![Component Pack](images/screenshot_component_test_frame.png)

### Window

To create a window, place a frame at the root level of the Figma file. The frame will be automatically converted into a
window.

### Naming Conventions

Component names must start with a prefix indicating their type. Component names are case-insensitive and disregard
spaces, dashes, and underscores (`  , -, _`).

| Component Type    | Prefix          |
|-------------------|-----------------|
| Button            | button          |
| Custom Button     | custombutton    |
| Text Field        | textfield       |
| Custom Text Field | customtextfield |
| Checkbox          | checkbox        |
| Tabs view         | tabsview        |
| Slider            | slider          |
| Progress Bar      | progressbar     |

### Hierarchy and Ordering

Some components require specific hierarchies to function correctly:

#### Button & Text Field

No specific hierarchy is needed for these components. Ensure correct naming.

#### Custom Button

The custom button group should follow this ordering:

| Child Index  | Child Function |
|--------------|----------------|
| -1 (Topmost) | MouseOver      |
| -2           | Pressed        |
| -3           | Disabled       |
| -4           | Normal         |
| ...          | Background...  |

Here is an example of a custom button group in Figma:
![Custom Button Group](images/screenshot_custom_button_instructions.png)

#### Custom Text Field

For custom text fields, maintain the following order:

| Child Index  | Child Function   |
|--------------|------------------|
| -1 (Topmost) | Text (for style) |
| -2           | Hint             |
| ...          | Background...    |

#### Checkbox

The checkbox group should be ordered as follows:

| Child Index  | Child Function |
|--------------|----------------|
| -1 (Topmost) | Checked        |
| ...          | Background...  |

#### Tabs View

The tabs view group requires the following ordering:

| Child Index  | Child Function |
|--------------|----------------|
| -1 (Topmost) | Tabs bar       |
| -2           | Tabs content   |
| ...          | Background...  |

Ensure that the tabs bar contains buttons for switching between tabs (in the selected version), and tabs content holds
the respective tab content.

Here is an example of a tabs view group in Figma:
![Tabs View Group](images/screenshot_tabs_view_instructions.png)

#### Slider

The slider group must follow this ordering:

| Child Index  | Child Function |
|--------------|----------------|
| -1 (Topmost) | Slider handle  |
| ...          | Background...  |

#### Progress Bar

For progress bars, maintain the following order:

| Child Index  | Child Function |
|--------------|----------------|
| -1 (Topmost) | Fill           |
| ...          | Background...  |

By adhering to these naming conventions and hierarchies, you can make the most of PyQt Figma Designer's capabilities to
create rich and functional PyQt6 GUIs.

### Writing Custom Components

To create custom components for your GUIs, follow these steps:

1. **Create a Python File**: Begin by creating a new Python file in the `generator/design/components` directory. This file will serve as the container for your custom component class.

2. **Inherit from `ComponentGenerator`**: In your Python file, define a class that inherits from the `ComponentGenerator` class found in `generator.design.component_generator`.

3. **Define Class Fields**:
   - `component_name`: Define a class field named `component_name`. This field specifies the prefix used to identify the component in the Figma file. Ensure this prefix is unique, case-insensitive, and doesn't conflict with existing components.
   - `component_config` (Optional): You can include an optional `component_config` field to extend the `component_config.py` file with additional configuration options. By default, this field should be an empty dictionary.

4. **Implement the `generate_design` Method**: This method is required and should generate the design and behavior of your custom component. Use the `generate_q_widget` function to create a `QWidget` object. You can access the component's properties using the `self.q_widget_name` syntax. Additionally, use the `generate_activate_handler` function to call the handler's methods once. Finally, utilize the `generate_link_controller` function to connect the controller's methods to your lambda functions.

5. **Implement the `generate_handler` Method** (Optional): This method is optional and should generate the handler's methods. Use the `generate_activate_handler` function to call the handler's methods from the generate_design function's generated code.

6. **Implement the `generate_controller` Method** (Optional): This method is also optional and should generate the controller's methods. Use the `generate_link_controller` from the generate_design function to establish links between the controller's methods and your lambda functions. Note that controller functions should be overridden by the GUI and have no impact on the generated code.

Here's an example of a custom component class:

```python
from generator.utils import generate_q_widget, generate_activate_handler, generate_link_controller, indent
from generator.design.component_generator import ComponentGenerator

class MyCustomComponent(ComponentGenerator):
    # Required: Component name
    component_name = "my_custom_component"
    # Optional: Component config
    component_config = {
        "enabled": True,
    }

    # Required method to generate design.
    def generate_design(self):
        # Create an empty QWidget object
        yield from generate_q_widget(self)
        
        # Set component properties
        yield f'self.{self.q_widget_name}.setEnabled(ComponentsConfig.{self.config_class_path}.enabled)'
        
        # Call the handler's methods once
        yield from generate_activate_handler(self, f'{self.short_class_name}_handler')
        
        # Link controller's methods to lambda functions
        lambda_function_name = f'{self.short_class_name}_lambda1'
        yield f'self.{lambda_function_name} = lambda: print("Lambda Function !")'
        yield from generate_link_controller(self, lambda_function_name, f'{self.short_class_name}_controller')
        
        # Create a button and link it to the handler function
        call_handler = '\n'.join(
            indent(
                generate_activate_handler(self, f'{self.short_class_name}_handler')
            )
        )
        yield f"""self.{self.q_widget_name}_button = QPushButton(self.{self.q_widget_name})
def __{self.short_class_name}_handler(self):
{call_handler}
self.{self.q_widget_name}_button.clicked.connect(__{self.short_class_name}_handler)""".splitlines()

    # Optional method to generate handler.
    def generate_handler(self):
        yield f'def {self.short_class_name}_handler(self):'
        yield f'    print("Handler Function !")'

    # Optional method to generate controller
    def generate_controller(self):
        yield f'def {self.short_class_name}_controller():'
        # The controller's functions should be overridden by the GUI
        # and then their code will have no impact.
        yield f'    pass'
```

You can find additional examples of custom components in the `generator/design/components` directory.

Feel free to read the documentation in the `generator.design.component_generator.ComponentGenerator` class for more
details.
```bash
python -m pydoc generator.design.component_generator.ComponentGenerator
```