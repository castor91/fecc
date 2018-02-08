from AbstractMoveInstruction import AbstractMoveInstruction as AMI


class MOVL(AMI):

    def __init__(self, src_value, dst_registry, is_registry=False):
        super(MOVL, self).__init__(src_value, dst_registry)
        self._is_registry = is_registry

    def generate(self):
        return 'movl {}{}, %{}'.format('%' if self._is_registry else '$', self._src_value, self._dst_registry)
