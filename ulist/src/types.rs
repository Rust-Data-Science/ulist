use crate::boolean::BooleanList;
use crate::floatings::FloatList32;
use crate::floatings::FloatList64;
use crate::integers::IntegerList32;
use crate::integers::IntegerList64;
use crate::string::StringList;

pub trait AsBooleanList {
    fn as_bool(&self) -> BooleanList;
}

pub trait AsFloatList32 {
    fn as_float32(&self) -> FloatList32;
}

pub trait AsFloatList64 {
    fn as_float64(&self) -> FloatList64;
}

pub trait AsIntegerList32 {
    fn as_int32(&self) -> IntegerList32;
}

pub trait AsIntegerList64 {
    fn as_int64(&self) -> IntegerList64;
}

pub trait AsStringList {
    fn as_str(&self) -> StringList;
}
