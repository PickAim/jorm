from abc import ABC, abstractmethod


class Initializable(ABC):
    pass


class Initializer(ABC):
    def __init__(self):
        """
        Declare your constructor to specify initializing parameters like:
            def __init__(self, special_param: SpecialType):
                super().__init__()
                self.special_param = special_param

        And use it in overriden _init_something method to init Initializable object
        """
        pass

    def init_object(self, initializable_object: Initializable) -> None:
        """
        Override if necessary specify initializable object type like:
            def init_object(self, initializable_object: MySpecifiedType):
                super().init_object(initializable_object)

        :param initializable_object: object that should be initialized
        :return: None
        """
        self._init_something(initializable_object)
        self._check_init(initializable_object)

    @abstractmethod
    def _init_something(self, initializable_object: Initializable) -> None:
        """
        Here should be your initialization logic
        :param initializable_object: object that should be initialized
        :return: None
        """
        pass

    def _check_init(self, initializable_object: Initializable) -> None:
        """
        Check that object initialized successfully using not None checks
        Override if needed another check
        :param initializable_object: object that should be already initialized
        :return: None
        """
        attributes = initializable_object.__dict__
        for attribute_key in attributes:
            if attributes[attribute_key] is None:
                raise Exception(
                    f"Attribute {attribute_key} of object of type {type(initializable_object)} is not initialized.")
