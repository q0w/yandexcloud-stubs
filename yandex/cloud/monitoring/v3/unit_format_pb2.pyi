"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _UnitFormat:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _UnitFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_UnitFormat.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNIT_FORMAT_UNSPECIFIED: _UnitFormat.ValueType  # 0
    UNIT_NONE: _UnitFormat.ValueType  # 1
    """Misc.

    None (show tick values as-is).
    """

    UNIT_COUNT: _UnitFormat.ValueType  # 2
    """Count."""

    UNIT_PERCENT: _UnitFormat.ValueType  # 3
    """Percent (0-100)."""

    UNIT_PERCENT_UNIT: _UnitFormat.ValueType  # 4
    """Percent (0-1)."""

    UNIT_NANOSECONDS: _UnitFormat.ValueType  # 5
    """Time.

    Nanoseconds (ns).
    """

    UNIT_MICROSECONDS: _UnitFormat.ValueType  # 6
    """Microseconds (µs)."""

    UNIT_MILLISECONDS: _UnitFormat.ValueType  # 7
    """Milliseconds (ms)."""

    UNIT_SECONDS: _UnitFormat.ValueType  # 8
    """Seconds (s)."""

    UNIT_MINUTES: _UnitFormat.ValueType  # 9
    """Minutes (m)."""

    UNIT_HOURS: _UnitFormat.ValueType  # 10
    """Hours (h)."""

    UNIT_DAYS: _UnitFormat.ValueType  # 11
    """Days (d)."""

    UNIT_BITS_SI: _UnitFormat.ValueType  # 12
    """Data (SI).

    Bits (SI).
    """

    UNIT_BYTES_SI: _UnitFormat.ValueType  # 13
    """Bytes (SI)."""

    UNIT_KILOBYTES: _UnitFormat.ValueType  # 14
    """Kilobytes (KB)."""

    UNIT_MEGABYTES: _UnitFormat.ValueType  # 15
    """Megabytes (MB)."""

    UNIT_GIGABYTES: _UnitFormat.ValueType  # 16
    """Gigabytes (GB)."""

    UNIT_TERABYTES: _UnitFormat.ValueType  # 17
    """Terabytes (TB)"""

    UNIT_PETABYTES: _UnitFormat.ValueType  # 18
    """Petabytes (PB)."""

    UNIT_EXABYTES: _UnitFormat.ValueType  # 19
    """Exabytes (EB)."""

    UNIT_BITS_IEC: _UnitFormat.ValueType  # 20
    """Data (IEC).

    Bits (IEC).
    """

    UNIT_BYTES_IEC: _UnitFormat.ValueType  # 21
    """Bytes (IEC)."""

    UNIT_KIBIBYTES: _UnitFormat.ValueType  # 22
    """Kibibytes (KiB)."""

    UNIT_MEBIBYTES: _UnitFormat.ValueType  # 23
    """Mebibytes (MiB)."""

    UNIT_GIBIBYTES: _UnitFormat.ValueType  # 24
    """Gigibytes (GiB)."""

    UNIT_TEBIBYTES: _UnitFormat.ValueType  # 25
    """Tebibytes (TiB)."""

    UNIT_PEBIBYTES: _UnitFormat.ValueType  # 26
    """Pebibytes (PiB)."""

    UNIT_EXBIBYTES: _UnitFormat.ValueType  # 27
    """Exbibytes (EiB)."""

    UNIT_REQUESTS_PER_SECOND: _UnitFormat.ValueType  # 28
    """Throughput.

    Requests per second (reqps).
    """

    UNIT_OPERATIONS_PER_SECOND: _UnitFormat.ValueType  # 29
    """Operations per second (ops)."""

    UNIT_WRITES_PER_SECOND: _UnitFormat.ValueType  # 30
    """Writes per second (wps)."""

    UNIT_READS_PER_SECOND: _UnitFormat.ValueType  # 31
    """Reads per second (rps)."""

    UNIT_PACKETS_PER_SECOND: _UnitFormat.ValueType  # 32
    """Packets per second (pps)."""

    UNIT_IO_OPERATIONS_PER_SECOND: _UnitFormat.ValueType  # 33
    """IO operations per second (iops)."""

    UNIT_COUNTS_PER_SECOND: _UnitFormat.ValueType  # 34
    """Counts per second (counts/sec)."""

    UNIT_BITS_SI_PER_SECOND: _UnitFormat.ValueType  # 35
    """Data Rate (SI).

    Bits (SI) per second (bits/sec).
    """

    UNIT_BYTES_SI_PER_SECOND: _UnitFormat.ValueType  # 36
    """Bytes (SI) per second (bytes/sec)."""

    UNIT_KILOBITS_PER_SECOND: _UnitFormat.ValueType  # 37
    """Kilobits per second (KBits/sec)."""

    UNIT_KILOBYTES_PER_SECOND: _UnitFormat.ValueType  # 38
    """Kilobytes per second (KB/sec)."""

    UNIT_MEGABITS_PER_SECOND: _UnitFormat.ValueType  # 39
    """Megabits per second (MBits/sec)."""

    UNIT_MEGABYTES_PER_SECOND: _UnitFormat.ValueType  # 40
    """Megabytes per second (MB/sec)."""

    UNIT_GIGABITS_PER_SECOND: _UnitFormat.ValueType  # 41
    """Gigabits per second (GBits/sec)."""

    UNIT_GIGABYTES_PER_SECOND: _UnitFormat.ValueType  # 42
    """Gigabytes per second (GB/sec)."""

    UNIT_TERABITS_PER_SECOND: _UnitFormat.ValueType  # 43
    """Terabits per second (TBits/sec)."""

    UNIT_TERABYTES_PER_SECOND: _UnitFormat.ValueType  # 44
    """Terabytes per second (TB/sec)."""

    UNIT_PETABITS_PER_SECOND: _UnitFormat.ValueType  # 45
    """Petabits per second (Pbits/sec)."""

    UNIT_PETABYTES_PER_SECOND: _UnitFormat.ValueType  # 46
    """Petabytes per second (PB/sec)."""

    UNIT_BITS_IEC_PER_SECOND: _UnitFormat.ValueType  # 47
    """Data Rate (IEC).

    Bits (IEC) per second (bits/sec).
    """

    UNIT_BYTES_IEC_PER_SECOND: _UnitFormat.ValueType  # 48
    """Bytes (IEC) per second (bytes/sec)."""

    UNIT_KIBIBITS_PER_SECOND: _UnitFormat.ValueType  # 49
    """Kibibits per second (KiBits/sec)."""

    UNIT_KIBIBYTES_PER_SECOND: _UnitFormat.ValueType  # 50
    """Kibibytes per second (KiB/sec)."""

    UNIT_MEBIBITS_PER_SECOND: _UnitFormat.ValueType  # 51
    """Mebibits per second (MiBits/sec)."""

    UNIT_MEBIBYTES_PER_SECOND: _UnitFormat.ValueType  # 52
    """Mebibytes per second (MiB/sec)."""

    UNIT_GIBIBITS_PER_SECOND: _UnitFormat.ValueType  # 53
    """Gibibits per second (GiBits/sec)."""

    UNIT_GIBIBYTES_PER_SECOND: _UnitFormat.ValueType  # 54
    """Gibibytes per second (GiB/sec)."""

    UNIT_TEBIBITS_PER_SECOND: _UnitFormat.ValueType  # 55
    """Tebibits per second (TiBits/sec)."""

    UNIT_TEBIBYTES_PER_SECOND: _UnitFormat.ValueType  # 56
    """Tebibytes per second (TiB/sec)."""

    UNIT_PEBIBITS_PER_SECOND: _UnitFormat.ValueType  # 57
    """Pebibits per second (PiBits/sec)."""

    UNIT_PEBIBYTES_PER_SECOND: _UnitFormat.ValueType  # 58
    """Pebibytes per second (PiB/sec)."""

    UNIT_DATETIME_UTC: _UnitFormat.ValueType  # 59
    """Date & time.

    Datetime (UTC).
    """

    UNIT_DATETIME_LOCAL: _UnitFormat.ValueType  # 60
    """Datetime (local)."""

    UNIT_HERTZ: _UnitFormat.ValueType  # 61
    """Frequency.

    Hertz (Hz).
    """

    UNIT_KILOHERTZ: _UnitFormat.ValueType  # 62
    """Kilohertz (KHz)."""

    UNIT_MEGAHERTZ: _UnitFormat.ValueType  # 63
    """Megahertz (MHz)."""

    UNIT_GIGAHERTZ: _UnitFormat.ValueType  # 64
    """Gigahertz (GHz)."""

    UNIT_DOLLAR: _UnitFormat.ValueType  # 65
    """Currency.

    Dollar.
    """

    UNIT_EURO: _UnitFormat.ValueType  # 66
    """Euro."""

    UNIT_ROUBLE: _UnitFormat.ValueType  # 67
    """Rouble."""

    UNIT_CELSIUS: _UnitFormat.ValueType  # 68
    """Temperature.

    Celsius (°C).
    """

    UNIT_FAHRENHEIT: _UnitFormat.ValueType  # 69
    """Fahrenheit (°F)."""

    UNIT_KELVIN: _UnitFormat.ValueType  # 70
    """Kelvin (K)."""

    UNIT_FLOP_PER_SECOND: _UnitFormat.ValueType  # 71
    """Computation.

    Flop per second (FLOP/sec).
    """

    UNIT_KILOFLOP_PER_SECOND: _UnitFormat.ValueType  # 72
    """Kiloflop per second (KFLOP/sec)."""

    UNIT_MEGAFLOP_PER_SECOND: _UnitFormat.ValueType  # 73
    """Megaflop per second (MFLOP/sec)."""

    UNIT_GIGAFLOP_PER_SECOND: _UnitFormat.ValueType  # 74
    """Gigaflop per second (GFLOP/sec)."""

    UNIT_PETAFLOP_PER_SECOND: _UnitFormat.ValueType  # 75
    """Petaflop per second (PFLOP/sec)."""

    UNIT_EXAFLOP_PER_SECOND: _UnitFormat.ValueType  # 76
    """Exaflop per second (EFLOP/sec)."""

    UNIT_METERS_PER_SECOND: _UnitFormat.ValueType  # 77
    """Velocity.

    Meters per second (m/sec).
    """

    UNIT_KILOMETERS_PER_HOUR: _UnitFormat.ValueType  # 78
    """Kilometers per hour (km/h)."""

    UNIT_MILES_PER_HOUR: _UnitFormat.ValueType  # 79
    """Miles per hour (mi/h)."""

    UNIT_MILLIMETER: _UnitFormat.ValueType  # 80
    """Length.

    Millimeter.
    """

    UNIT_CENTIMETER: _UnitFormat.ValueType  # 81
    """Centimeter."""

    UNIT_METER: _UnitFormat.ValueType  # 82
    """Meter."""

    UNIT_KILOMETER: _UnitFormat.ValueType  # 83
    """Kilometer."""

    UNIT_MILE: _UnitFormat.ValueType  # 84
    """Mile."""

    UNIT_PPM: _UnitFormat.ValueType  # 85
    """Concentration.

    Parts per million (ppm).
    """

    UNIT_EVENTS_PER_SECOND: _UnitFormat.ValueType  # 86
    """Events per second"""

    UNIT_PACKETS: _UnitFormat.ValueType  # 87
    """Packets"""

    UNIT_DBM: _UnitFormat.ValueType  # 88
    """dBm (dbm)"""

    UNIT_VIRTUAL_CPU: _UnitFormat.ValueType  # 89
    """Virtual CPU cores based on CPU time (vcpu)"""

    UNIT_MESSAGES_PER_SECOND: _UnitFormat.ValueType  # 90
    """Messages per second (mps)"""

class UnitFormat(_UnitFormat, metaclass=_UnitFormatEnumTypeWrapper):
    pass

UNIT_FORMAT_UNSPECIFIED: UnitFormat.ValueType  # 0
UNIT_NONE: UnitFormat.ValueType  # 1
"""Misc.

None (show tick values as-is).
"""

UNIT_COUNT: UnitFormat.ValueType  # 2
"""Count."""

UNIT_PERCENT: UnitFormat.ValueType  # 3
"""Percent (0-100)."""

UNIT_PERCENT_UNIT: UnitFormat.ValueType  # 4
"""Percent (0-1)."""

UNIT_NANOSECONDS: UnitFormat.ValueType  # 5
"""Time.

Nanoseconds (ns).
"""

UNIT_MICROSECONDS: UnitFormat.ValueType  # 6
"""Microseconds (µs)."""

UNIT_MILLISECONDS: UnitFormat.ValueType  # 7
"""Milliseconds (ms)."""

UNIT_SECONDS: UnitFormat.ValueType  # 8
"""Seconds (s)."""

UNIT_MINUTES: UnitFormat.ValueType  # 9
"""Minutes (m)."""

UNIT_HOURS: UnitFormat.ValueType  # 10
"""Hours (h)."""

UNIT_DAYS: UnitFormat.ValueType  # 11
"""Days (d)."""

UNIT_BITS_SI: UnitFormat.ValueType  # 12
"""Data (SI).

Bits (SI).
"""

UNIT_BYTES_SI: UnitFormat.ValueType  # 13
"""Bytes (SI)."""

UNIT_KILOBYTES: UnitFormat.ValueType  # 14
"""Kilobytes (KB)."""

UNIT_MEGABYTES: UnitFormat.ValueType  # 15
"""Megabytes (MB)."""

UNIT_GIGABYTES: UnitFormat.ValueType  # 16
"""Gigabytes (GB)."""

UNIT_TERABYTES: UnitFormat.ValueType  # 17
"""Terabytes (TB)"""

UNIT_PETABYTES: UnitFormat.ValueType  # 18
"""Petabytes (PB)."""

UNIT_EXABYTES: UnitFormat.ValueType  # 19
"""Exabytes (EB)."""

UNIT_BITS_IEC: UnitFormat.ValueType  # 20
"""Data (IEC).

Bits (IEC).
"""

UNIT_BYTES_IEC: UnitFormat.ValueType  # 21
"""Bytes (IEC)."""

UNIT_KIBIBYTES: UnitFormat.ValueType  # 22
"""Kibibytes (KiB)."""

UNIT_MEBIBYTES: UnitFormat.ValueType  # 23
"""Mebibytes (MiB)."""

UNIT_GIBIBYTES: UnitFormat.ValueType  # 24
"""Gigibytes (GiB)."""

UNIT_TEBIBYTES: UnitFormat.ValueType  # 25
"""Tebibytes (TiB)."""

UNIT_PEBIBYTES: UnitFormat.ValueType  # 26
"""Pebibytes (PiB)."""

UNIT_EXBIBYTES: UnitFormat.ValueType  # 27
"""Exbibytes (EiB)."""

UNIT_REQUESTS_PER_SECOND: UnitFormat.ValueType  # 28
"""Throughput.

Requests per second (reqps).
"""

UNIT_OPERATIONS_PER_SECOND: UnitFormat.ValueType  # 29
"""Operations per second (ops)."""

UNIT_WRITES_PER_SECOND: UnitFormat.ValueType  # 30
"""Writes per second (wps)."""

UNIT_READS_PER_SECOND: UnitFormat.ValueType  # 31
"""Reads per second (rps)."""

UNIT_PACKETS_PER_SECOND: UnitFormat.ValueType  # 32
"""Packets per second (pps)."""

UNIT_IO_OPERATIONS_PER_SECOND: UnitFormat.ValueType  # 33
"""IO operations per second (iops)."""

UNIT_COUNTS_PER_SECOND: UnitFormat.ValueType  # 34
"""Counts per second (counts/sec)."""

UNIT_BITS_SI_PER_SECOND: UnitFormat.ValueType  # 35
"""Data Rate (SI).

Bits (SI) per second (bits/sec).
"""

UNIT_BYTES_SI_PER_SECOND: UnitFormat.ValueType  # 36
"""Bytes (SI) per second (bytes/sec)."""

UNIT_KILOBITS_PER_SECOND: UnitFormat.ValueType  # 37
"""Kilobits per second (KBits/sec)."""

UNIT_KILOBYTES_PER_SECOND: UnitFormat.ValueType  # 38
"""Kilobytes per second (KB/sec)."""

UNIT_MEGABITS_PER_SECOND: UnitFormat.ValueType  # 39
"""Megabits per second (MBits/sec)."""

UNIT_MEGABYTES_PER_SECOND: UnitFormat.ValueType  # 40
"""Megabytes per second (MB/sec)."""

UNIT_GIGABITS_PER_SECOND: UnitFormat.ValueType  # 41
"""Gigabits per second (GBits/sec)."""

UNIT_GIGABYTES_PER_SECOND: UnitFormat.ValueType  # 42
"""Gigabytes per second (GB/sec)."""

UNIT_TERABITS_PER_SECOND: UnitFormat.ValueType  # 43
"""Terabits per second (TBits/sec)."""

UNIT_TERABYTES_PER_SECOND: UnitFormat.ValueType  # 44
"""Terabytes per second (TB/sec)."""

UNIT_PETABITS_PER_SECOND: UnitFormat.ValueType  # 45
"""Petabits per second (Pbits/sec)."""

UNIT_PETABYTES_PER_SECOND: UnitFormat.ValueType  # 46
"""Petabytes per second (PB/sec)."""

UNIT_BITS_IEC_PER_SECOND: UnitFormat.ValueType  # 47
"""Data Rate (IEC).

Bits (IEC) per second (bits/sec).
"""

UNIT_BYTES_IEC_PER_SECOND: UnitFormat.ValueType  # 48
"""Bytes (IEC) per second (bytes/sec)."""

UNIT_KIBIBITS_PER_SECOND: UnitFormat.ValueType  # 49
"""Kibibits per second (KiBits/sec)."""

UNIT_KIBIBYTES_PER_SECOND: UnitFormat.ValueType  # 50
"""Kibibytes per second (KiB/sec)."""

UNIT_MEBIBITS_PER_SECOND: UnitFormat.ValueType  # 51
"""Mebibits per second (MiBits/sec)."""

UNIT_MEBIBYTES_PER_SECOND: UnitFormat.ValueType  # 52
"""Mebibytes per second (MiB/sec)."""

UNIT_GIBIBITS_PER_SECOND: UnitFormat.ValueType  # 53
"""Gibibits per second (GiBits/sec)."""

UNIT_GIBIBYTES_PER_SECOND: UnitFormat.ValueType  # 54
"""Gibibytes per second (GiB/sec)."""

UNIT_TEBIBITS_PER_SECOND: UnitFormat.ValueType  # 55
"""Tebibits per second (TiBits/sec)."""

UNIT_TEBIBYTES_PER_SECOND: UnitFormat.ValueType  # 56
"""Tebibytes per second (TiB/sec)."""

UNIT_PEBIBITS_PER_SECOND: UnitFormat.ValueType  # 57
"""Pebibits per second (PiBits/sec)."""

UNIT_PEBIBYTES_PER_SECOND: UnitFormat.ValueType  # 58
"""Pebibytes per second (PiB/sec)."""

UNIT_DATETIME_UTC: UnitFormat.ValueType  # 59
"""Date & time.

Datetime (UTC).
"""

UNIT_DATETIME_LOCAL: UnitFormat.ValueType  # 60
"""Datetime (local)."""

UNIT_HERTZ: UnitFormat.ValueType  # 61
"""Frequency.

Hertz (Hz).
"""

UNIT_KILOHERTZ: UnitFormat.ValueType  # 62
"""Kilohertz (KHz)."""

UNIT_MEGAHERTZ: UnitFormat.ValueType  # 63
"""Megahertz (MHz)."""

UNIT_GIGAHERTZ: UnitFormat.ValueType  # 64
"""Gigahertz (GHz)."""

UNIT_DOLLAR: UnitFormat.ValueType  # 65
"""Currency.

Dollar.
"""

UNIT_EURO: UnitFormat.ValueType  # 66
"""Euro."""

UNIT_ROUBLE: UnitFormat.ValueType  # 67
"""Rouble."""

UNIT_CELSIUS: UnitFormat.ValueType  # 68
"""Temperature.

Celsius (°C).
"""

UNIT_FAHRENHEIT: UnitFormat.ValueType  # 69
"""Fahrenheit (°F)."""

UNIT_KELVIN: UnitFormat.ValueType  # 70
"""Kelvin (K)."""

UNIT_FLOP_PER_SECOND: UnitFormat.ValueType  # 71
"""Computation.

Flop per second (FLOP/sec).
"""

UNIT_KILOFLOP_PER_SECOND: UnitFormat.ValueType  # 72
"""Kiloflop per second (KFLOP/sec)."""

UNIT_MEGAFLOP_PER_SECOND: UnitFormat.ValueType  # 73
"""Megaflop per second (MFLOP/sec)."""

UNIT_GIGAFLOP_PER_SECOND: UnitFormat.ValueType  # 74
"""Gigaflop per second (GFLOP/sec)."""

UNIT_PETAFLOP_PER_SECOND: UnitFormat.ValueType  # 75
"""Petaflop per second (PFLOP/sec)."""

UNIT_EXAFLOP_PER_SECOND: UnitFormat.ValueType  # 76
"""Exaflop per second (EFLOP/sec)."""

UNIT_METERS_PER_SECOND: UnitFormat.ValueType  # 77
"""Velocity.

Meters per second (m/sec).
"""

UNIT_KILOMETERS_PER_HOUR: UnitFormat.ValueType  # 78
"""Kilometers per hour (km/h)."""

UNIT_MILES_PER_HOUR: UnitFormat.ValueType  # 79
"""Miles per hour (mi/h)."""

UNIT_MILLIMETER: UnitFormat.ValueType  # 80
"""Length.

Millimeter.
"""

UNIT_CENTIMETER: UnitFormat.ValueType  # 81
"""Centimeter."""

UNIT_METER: UnitFormat.ValueType  # 82
"""Meter."""

UNIT_KILOMETER: UnitFormat.ValueType  # 83
"""Kilometer."""

UNIT_MILE: UnitFormat.ValueType  # 84
"""Mile."""

UNIT_PPM: UnitFormat.ValueType  # 85
"""Concentration.

Parts per million (ppm).
"""

UNIT_EVENTS_PER_SECOND: UnitFormat.ValueType  # 86
"""Events per second"""

UNIT_PACKETS: UnitFormat.ValueType  # 87
"""Packets"""

UNIT_DBM: UnitFormat.ValueType  # 88
"""dBm (dbm)"""

UNIT_VIRTUAL_CPU: UnitFormat.ValueType  # 89
"""Virtual CPU cores based on CPU time (vcpu)"""

UNIT_MESSAGES_PER_SECOND: UnitFormat.ValueType  # 90
"""Messages per second (mps)"""

global___UnitFormat = UnitFormat

