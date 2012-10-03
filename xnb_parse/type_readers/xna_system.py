"""
system type readers
"""

from xnb_parse.type_reader_manager import TypeReaderPlugin
from xnb_parse.type_reader import ValueTypeReader, GenericTypeReader, GenericValueTypeReader


class EnumReader(GenericValueTypeReader, TypeReaderPlugin):
    generic_target_type = u'System.Enum`1'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.EnumReader`1'

    def read(self):
        return self.readers[0].read()


class NullableReader(GenericValueTypeReader, TypeReaderPlugin):
    generic_target_type = u'System.Nullable`1'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.NullableReader`1'

    def read(self):
        has_value = self.stream.read_boolean()
        if has_value:
            return self.readers[0].read()
        else:
            return None


class ArrayReader(GenericTypeReader, TypeReaderPlugin):
    generic_target_type = u'System.Array`1'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.ArrayReader`1'

    def read(self):
        elements = self.stream.read_int32()
        values = []
        for _ in range(elements):
            element = self.stream.read_value_or_object(self.readers[0])
            values.append(element)
        return values


class ListReader(GenericTypeReader, TypeReaderPlugin):
    generic_target_type = u'System.Collections.Generic.List`1'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.ListReader`1'

    def read(self):
        elements = self.stream.read_int32()
        values = []
        for _ in range(elements):
            element = self.stream.read_value_or_object(self.readers[0])
            values.append(element)
        return values


class DictionaryReader(GenericTypeReader, TypeReaderPlugin):
    generic_target_type = u'System.Collections.Generic.Dictionary`2'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.DictionaryReader`2'

    def read(self):
        elements = self.stream.read_int32()
        values = {}
        for _ in range(elements):
            key = self.stream.read_value_or_object(self.readers[0])
            value = self.stream.read_value_or_object(self.readers[1])
            values[key] = value
        return values


class TimeSpanReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'System.TimeSpan'
    reader_name = u'Microsoft.Xna.Framework.Content.TimeSpanReader'

    def read(self):
        ticks = self.stream.read_int64()
        return ticks


class DateTimeReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'System.DateTime'
    reader_name = u'Microsoft.Xna.Framework.Content.DateTimeReader'

    def read(self):
        value = self.stream.read_int64()
        return value


class DecimalReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'System.Decimal'
    reader_name = u'Microsoft.Xna.Framework.Content.DecimalReader'

    def read(self):
        v_a = self.stream.read_int32()
        v_b = self.stream.read_int32()
        v_c = self.stream.read_int32()
        v_d = self.stream.read_int32()
        return v_a, v_b, v_c, v_d


class ExternalReferenceReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'ExternalReference'
    reader_name = u'Microsoft.Xna.Framework.Content.ExternalReferenceReader'

    def read(self):
        return self.stream.read_external_reference()


class ReflectiveReader(GenericTypeReader, TypeReaderPlugin):
    generic_target_type = u'Reflective'
    generic_reader_name = u'Microsoft.Xna.Framework.Content.ReflectiveReader`1'

    def read(self):
        return self.readers[0].read()
