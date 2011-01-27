#include <exception.hpp>

namespace Iliad {

class Log {

public:
	virtual ~Log();

	virtual void operator()(Iliad::Exception& e) = 0;

protected:
	Log();

};

}
