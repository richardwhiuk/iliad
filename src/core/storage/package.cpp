#include <iliad.hpp>

#include <core/storage/package.hpp>

Iliad::Core::Storage::Package::Package(Iliad::Server& server) : Iliad::Package::Package(server) {

}

Iliad::Core::Storage::Package::~Package(){

}

std::string Iliad::Core::Storage::Package::name(){
	return "Storage";
}

std::map<std::string, Iliad::Module*> Iliad::Core::Storage::Package::modules(){
	std::map<std::string, Iliad::Module*> modules;

	return modules;
}

