from AbstractMoveInstruction import AbstractMoveInstruction as AMI


class MOVL(AMI):

    def __init__(self, src_value, dst_registry):
        super(MOVL, self).__init__(src_value, dst_registry)

    def generate(self):
        return 'movl ${}, %{}'.format(self._src_value, self._dst_registry)
