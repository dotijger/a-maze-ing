

class GenerationError(BaseException):
    
    def __init__(self, message: str = "Unknown Generation Error", f: str | None = None) -> None:
        self.message = message
        self.function = f
        super().__init__(self.message)

    def __str__(self) -> str:
        if self.function is not None:
            return f"Generation Error! {self.message} in function {self.function}"
        return f"Generation Error! {self.message}"


class SolveError(BaseException):
    
    def __init__(self, message="Unknown Solving Error", f: str | None = None) -> None:
        self.message = message
        self.function = f
        super().__init__(self.message)

    def __str__(self) -> str:
        if self.function is not None:
            return f"Solving Error! {self.message} in function {self.function}"
        return f"Solving Error! {self.message}"
