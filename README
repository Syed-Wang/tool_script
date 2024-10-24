# 工具脚本

## 1. 说明

本目录下的脚本是一些工具脚本，用于辅助配置、开发或测试。

## 2. 脚本列表

| 文件名                                    | 说明                                                       |
| ----------------------------------------- | ---------------------------------------------------------- |
| [config_defines.py](#21-config_definespy) | 协助配置 `c_cpp_properties.json`，使 VSCode 能正确分析文件 |

### 2.1 config_defines.py

前置条件：VSCode 安装了 C/C++ 插件。并且在 `c_cpp_properties.json` 文件中正确配置 `includePath` 字段。

说明：在使用 VSCode 进行驱动开发时，因为使用了内核代码，IntelliSense 经常无法正确分析文件，导致编辑器报错，虽然和编译无关，但影响开发效率。这个脚本根据内核配置文件 `.config`，生成一个预处理器定义列表（宏定义），将这个列表添加到 VSCode 的配置文件`c_cpp_properties.json`中，IntelliSense 就能够正确分析文件了。

使用方法：

1. 执行脚本：`python config_defines.py <input_file_path> <output_file_path>`

   > `input_file_path`: 内核配置文件 `.config` 的路径
   > `output_file_path`: 生成文件的路径。

2. 在 `c_cpp_properties.json` 中的 `defines` 字段中。

   - 先添加以下内容：

     ```json
     "__GNUC__",
     "__KERNEL__",
     "__CHECKER__",
     "MODULE",
     ```

   - 然后将生成的宏定义列表添加到 `defines` 字段中，如：

     ```json
     "defines": [
                 "__GNUC__",
                 "__KERNEL__",
                 "__CHECKER__",
                 "MODULE",
                 "CONFIG_ARM",
                 "CONFIG_ARM_HAS_SG_CHAIN",
                 "CONFIG_MIGHT_HAVE_PCI",
                 "CONFIG_SYS_SUPPORTS_APM_EMULATION",
                 // ...
                 // ...
     ]
     ```
