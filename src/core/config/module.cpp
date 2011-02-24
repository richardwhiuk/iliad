#include <core/config/module.hpp>

Iliad::Core::Config::Module::Module(Iliad::Server& server) : Iliad::Module(server) {

}

Iliad::Core::Config::Module::~Module(){

}

std::string Iliad::Core::Config::Module::name(){
	return "Config";
}
