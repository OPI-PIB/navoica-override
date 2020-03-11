# from cms.djangoapps.contentstore.courseware_index import CourseAboutSearchIndexer,SearchIndexingError, CoursewareSearchIndexer, LibrarySearchIndexer,AboutInfo
from cms.djangoapps.contentstore.courseware_index import *

class CourseAboutSearchIndexer(CourseAboutSearchIndexer):

    ABOUT_INFORMATION_TO_INCLUDE = CourseAboutSearchIndexer.ABOUT_INFORMATION_TO_INCLUDE + [AboutInfo("organizer", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),
        AboutInfo("difficulty", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),
        AboutInfo("course_category", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),

        AboutInfo("is_new", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),
        AboutInfo("main_page", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),

        AboutInfo("availability", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),
        AboutInfo("self_paced", AboutInfo.PROPERTY, AboutInfo.FROM_COURSE_PROPERTY),]

class CoursewareSearchIndexer(CoursewareSearchIndexer):
    pass

class LibrarySearchIndexer(LibrarySearchIndexer):
    pass

class SearchIndexingError(SearchIndexingError):
    pass

class SearchIndexerBase(SearchIndexerBase):
    pass

class AboutInfo(AboutInfo):
    pass
