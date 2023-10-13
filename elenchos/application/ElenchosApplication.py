from cleo.application import Application

from elenchos.application.ElenchosCommandLoader import ElenchosCommandLoader


class ElenchosApplication(Application):
    """
    The Élenchos application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        Application.__init__(self, 'Élenchos', '0.0.1')

        self._command_loader = ElenchosCommandLoader()

# ----------------------------------------------------------------------------------------------------------------------
