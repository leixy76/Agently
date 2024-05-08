# 入口类型
EXECUTOR_TYPE_START = 'Start'
# 结束类型
EXECUTOR_TYPE_END = 'End'
# 常规类型
EXECUTOR_TYPE_NORMAL = 'Normal'

# workflow 初始数据的句柄名
WORKFLOW_START_DATA_HANDLE_NAME = f'WORKFLOW_SYS_DATA:{EXECUTOR_TYPE_START}'

# 默认的输入 handle
DEFAULT_INPUT_HANDLE_VALUE = 'input'
DEFAULT_INPUT_HANDLE = {'handle': DEFAULT_INPUT_HANDLE_VALUE, 'title': 'input'}
# 默认的输出 handle
DEFAULT_OUTPUT_HANDLE_VALUE = 'output'
DEFAULT_OUTPUT_HANDLE = {'handle': DEFAULT_OUTPUT_HANDLE_VALUE, 'title': 'output'}
