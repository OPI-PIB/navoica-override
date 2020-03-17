from edx_platform.cms.djangoapps.models.settings.course_metadata import CourseMetadata

class CourseMetadata(CourseMetadata):
    FILTERED_LIST = CourseMetadata.FILTERED_LIST + ['difficulty',
        'organizer',
        'course_category',
        'timetable',]
