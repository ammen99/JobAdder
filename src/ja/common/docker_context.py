'''
Contains definitions of the docker context of a job.
'''
from abc import ABC, abstractmethod
from typing import List


class MountPoint:
    '''
    A mount point consists of:
    1. A directory to be mounted.
    2. The target path in the Docker container where the directory needs to be
    mounted.
    '''
    def __init__(self, source: str, target: str):
        '''
        Initializes a new mount point.
        @source The directory to be mounted.
        @target The target path in the container to mount at.
        '''

    @property
    def source_path(self) -> str:
        '''
        @return The directory to be mounted.
        '''

    @property
    def mount_path(self) -> str:
        '''
        @return The path where the directory should be mounted.
        '''


class IDockerContext(ABC):
    '''
    A docker context consists of the necessary data to build a docker image to
    run a job in.
    '''

    @abstractmethod
    def get_dockerfile_source(self) -> str:
        '''
        @return The string contents of a Dockerfile which can be used to build
        the docker image.
        '''

    @abstractmethod
    def get_mount_points(self) -> List[MountPoint]:
        '''
        @return A list of all mount points for the job.
        '''


class DockerConstraints:
    '''
    A list of constraints of the docker container.
    '''
    def __init__(self, count_threads: int = -1, memory: int = 1):
        '''
        Create a new set of Docker constraints.
        memory is measured in MB.
        '''

    @property
    def cpu_threads(self) -> int:
        '''
        The maximum number of CPU threads the docker container can have.
        -1 means that the amount of threads is not set, in which case the
        number of threads will be determined when scheduling the job.
        '''

    @cpu_threads.setter
    def cpu_threads(self, count_threads: int) -> None:
        '''
        Set the number of CPU threads.
        If the number of cpu threads is already set(i.e it is not equal to -1),
        this will raise a RuntimeError.
        '''

    @property
    def memory(self) -> int:
        '''
        The maximum amount of RAM in MB to allocate for this container.
        '''
