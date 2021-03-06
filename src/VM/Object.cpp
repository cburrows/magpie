#include "Object.h"

namespace magpie
{
  using std::ostream;

  temp<BoolObject> Object::create(bool value)
  {
    return Memory::makeTemp(new BoolObject(value));
  }
  
  temp<NumberObject> Object::create(double value)
  {
    return Memory::makeTemp(new NumberObject(value));
  }
}
