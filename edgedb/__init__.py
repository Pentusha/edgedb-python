#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2016-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


# flake8: noqa

from ._version import __version__

from edgedb.datatypes.datatypes import (
    Tuple, NamedTuple, EnumValue, RelativeDuration, DateDuration, ConfigMemory
)
from edgedb.datatypes.datatypes import Set, Object, Array, Link, LinkSet
from edgedb.datatypes.range import Range

from .abstract import (
    Executor, AsyncIOExecutor, ReadOnlyExecutor, AsyncIOReadOnlyExecutor
)

from .asyncio_client import (
    create_async_client,
    AsyncIOClient
)

from .blocking_client import create_client, Client
from .options import RetryCondition, IsolationLevel, default_backoff
from .options import RetryOptions, TransactionOptions
from .options import State

from .errors._base import EdgeDBError, EdgeDBMessage


# The below is generated by `make gen-errors`.
# DO NOT MODIFY BY HAND.
#
# <ERRORS-AUTOGEN>
from .errors import (
    InternalServerError,
    UnsupportedFeatureError,
    ProtocolError,
    BinaryProtocolError,
    UnsupportedProtocolVersionError,
    TypeSpecNotFoundError,
    UnexpectedMessageError,
    InputDataError,
    ResultCardinalityMismatchError,
    CapabilityError,
    UnsupportedCapabilityError,
    DisabledCapabilityError,
    QueryError,
    InvalidSyntaxError,
    EdgeQLSyntaxError,
    SchemaSyntaxError,
    GraphQLSyntaxError,
    InvalidTypeError,
    InvalidTargetError,
    InvalidLinkTargetError,
    InvalidPropertyTargetError,
    InvalidReferenceError,
    UnknownModuleError,
    UnknownLinkError,
    UnknownPropertyError,
    UnknownUserError,
    UnknownDatabaseError,
    UnknownParameterError,
    SchemaError,
    SchemaDefinitionError,
    InvalidDefinitionError,
    InvalidModuleDefinitionError,
    InvalidLinkDefinitionError,
    InvalidPropertyDefinitionError,
    InvalidUserDefinitionError,
    InvalidDatabaseDefinitionError,
    InvalidOperatorDefinitionError,
    InvalidAliasDefinitionError,
    InvalidFunctionDefinitionError,
    InvalidConstraintDefinitionError,
    InvalidCastDefinitionError,
    DuplicateDefinitionError,
    DuplicateModuleDefinitionError,
    DuplicateLinkDefinitionError,
    DuplicatePropertyDefinitionError,
    DuplicateUserDefinitionError,
    DuplicateDatabaseDefinitionError,
    DuplicateOperatorDefinitionError,
    DuplicateViewDefinitionError,
    DuplicateFunctionDefinitionError,
    DuplicateConstraintDefinitionError,
    DuplicateCastDefinitionError,
    QueryTimeoutError,
    ExecutionError,
    InvalidValueError,
    DivisionByZeroError,
    NumericOutOfRangeError,
    IntegrityError,
    ConstraintViolationError,
    CardinalityViolationError,
    MissingRequiredError,
    TransactionError,
    TransactionConflictError,
    TransactionSerializationError,
    TransactionDeadlockError,
    ConfigurationError,
    AccessError,
    AuthenticationError,
    LogMessage,
    WarningMessage,
    ClientError,
    ClientConnectionError,
    ClientConnectionFailedError,
    ClientConnectionFailedTemporarilyError,
    ClientConnectionTimeoutError,
    ClientConnectionClosedError,
    InterfaceError,
    QueryArgumentError,
    MissingArgumentError,
    UnknownArgumentError,
    InvalidArgumentError,
    NoDataError,
)
# </ERRORS-AUTOGEN>
