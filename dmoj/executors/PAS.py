from dmoj.executors.base_executor import CompiledExecutor
from dmoj.executors.mixins import NullStdoutMixin


class Executor(NullStdoutMixin, CompiledExecutor):
    ext = '.pas'
    name = 'PAS'
    command = 'fpc'
    fs = ['/etc/timezone$']
    syscalls = ['select']
    command_paths = ['fpc']
    test_program = '''\
var line : string;
begin
    readln(line);
    writeln(line);
end.
'''

    def get_compile_args(self):
        return [self.get_command(), '-Fe/dev/stderr', '-So', '-O2', self._code]

    def get_compile_output(self, process):
        output = process.communicate()[1]
        return output if 'Fatal:' in output or 'Warning:' in output or 'Note:' in output else ''

    @classmethod
    def get_version_flags(cls, command):
        return ['-help']
