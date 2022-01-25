use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::integer::IntegerList;
use crate::string::StringList;

pub trait AsBooleanList {
    fn as_bool(&self) -> BooleanList;
}

pub trait AsFloatList {
    fn as_float(&self) -> FloatList;
}

pub trait AsIntegerList {
    fn as_int(&self) -> IntegerList;
}

pub trait AsStringList {
    fn as_str(&self) -> StringList;
}
