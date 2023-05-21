from enum import Enum

CAN_NOT_VALIDATE_REQUEST_QUERY = 'Cannot validate request query'


class AppError(Enum):
    pass


class ApiError(AppError):
    CANNOT_COMPLETE_REQUEST = 'Cannot complete request'
