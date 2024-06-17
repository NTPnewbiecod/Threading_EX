# comment hre
import _thread


thread_lock = _thread.allocate_lock()


class Threading():
    def __init__(self, target, args: tuple = (), kwargs: dict = {}) -> None:
        """This is Thread constructor.

        Args:
            target (func): function for thread to run.
            args (tuple, optional): argument to pass to the function. Defaults to ().
            kwargs (dict, optional): keyword argument to pass to the function. Defaults to {}.
        """
        self.target: function = target
        self.args = args
        self.kwargs = kwargs
        self._isDoneYetFlag: bool = False

        self._returnValue = None

    def _target_wrapper_DO_NOT_TOUCH(self, *args, **kwargs) -> None:
        self._returnValue = self.target(*args, **kwargs)
        self._isDoneYetFlag = True

    def start(self) -> None:
        """start current thread obj
        """
        _thread.start_new_thread(
            self._target_wrapper_DO_NOT_TOUCH, self.args, self.kwargs)

    def join(self):
        """Wait until the thread terminates and also return the value from the target function. 
        IMPORTANT target function MUST NOT have a "return" statement in side a loop.

        Returns:
            any: return value from the target function from thread that has been terminates. else return None
        """
        while not self._isDoneYetFlag:
            pass
        else:
            return self._returnValue

    def getReturnVal(self):
        """immediately return current value from the threading obj's internal "_return_value" value. 
        This function is intended to use alongside with "_push_return_val" function. 
        Race condition is already handle by it self.

        Returns:
            any: return value from the threading obj's internal copy of target function return value. else return None
        """
        with thread_lock:
            return self._returnValue

    def pushReturnVal(self, val):
        """immediately set current value of the threading obj's internal "_return_value" to the argument value. 
        This function is intended to use alongside with "_get_return_val" function. 
        Note: This function is in intended to use as a replacement for "return" statement in side a loop. 
        Race condition is already handle by it self.

        Args:
            val (any): value for threading obj's internal "_return_value" value to set to.
        """

        with thread_lock:
            self._returnValue = val
