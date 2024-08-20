const translation = {
  list: {
    title: 'اسناد',
    desc: 'تمامی فایل‌های دانش در اینجا نمایش داده می‌شوند و کل دانش می‌تواند به ارجاعات Mlchain متصل شود یا از طریق افزونه چت ایندکس شود.',
    addFile: 'اضافه کردن فایل',
    addPages: 'اضافه کردن صفحات',
    addUrl: 'اضافه کردن URL',
    table: {
      header: {
        fileName: 'نام فایل',
        words: 'کلمات',
        hitCount: 'تعداد بازیابی',
        uploadTime: 'زمان بارگذاری',
        status: 'وضعیت',
        action: 'اقدام',
      },
      rename: 'تغییر نام',
      name: 'نام',
    },
    action: {
      uploadFile: 'بارگذاری فایل جدید',
      settings: 'تنظیمات بخش‌بندی',
      addButton: 'اضافه کردن قطعه',
      add: 'اضافه کردن یک قطعه',
      batchAdd: 'افزودن گروهی',
      archive: 'بایگانی',
      unarchive: 'خارج کردن از بایگانی',
      delete: 'حذف',
      enableWarning: 'فایل بایگانی شده نمی‌تواند فعال شود',
      sync: 'همگام‌سازی',
    },
    index: {
      enable: 'فعال کردن',
      disable: 'غیرفعال کردن',
      all: 'همه',
      enableTip: 'فایل می‌تواند ایندکس شود',
      disableTip: 'فایل نمی‌تواند ایندکس شود',
    },
    status: {
      queuing: 'در صف',
      indexing: 'ایندکس‌سازی',
      paused: 'متوقف شده',
      error: 'خطا',
      available: 'موجود',
      enabled: 'فعال شده',
      disabled: 'غیرفعال شده',
      archived: 'بایگانی شده',
    },
    empty: {
      title: 'هنوز هیچ سندی وجود ندارد',
      upload: {
        tip: 'شما می‌توانید فایل‌ها را بارگذاری کنید، از وب‌سایت همگام‌سازی کنید، یا از برنامه‌های وبی مانند Notion، GitHub و غیره.',
      },
      sync: {
        tip: 'Mlchain به‌طور دوره‌ای فایل‌ها را از Notion شما دانلود و پردازش را کامل می‌کند.',
      },
    },
    delete: {
      title: 'آیا مطمئن هستید که حذف شود؟',
      content: 'اگر بعداً نیاز به ادامه پردازش داشتید، از همان جایی که مانده بودید ادامه می‌دهید',
    },
    batchModal: {
      title: 'افزودن گروهی قطعات',
      csvUploadTitle: 'فایل CSV خود را اینجا بکشید و رها کنید، یا ',
      browse: 'مرور کنید',
      tip: 'فایل CSV باید به ساختار زیر مطابقت داشته باشد:',
      question: 'سؤال',
      answer: 'پاسخ',
      contentTitle: 'محتوای قطعه',
      content: 'محتوا',
      template: 'الگو را از اینجا دانلود کنید',
      cancel: 'لغو',
      run: 'اجرای گروهی',
      runError: 'اجرای گروهی ناموفق بود',
      processing: 'در حال پردازش گروهی',
      completed: 'واردات کامل شد',
      error: 'خطای واردات',
      ok: 'تأیید',
    },
  },
  metadata: {
    title: 'اطلاعات متا',
    desc: 'برچسب‌گذاری متادیتا برای اسناد به هوش مصنوعی اجازه می‌دهد تا به موقع به آن‌ها دسترسی پیدا کند و منبع ارجاعات را برای کاربران آشکار کند.',
    dateTimeFormat: 'D MMMM YYYY hh:mm A',
    docTypeSelectTitle: 'لطفاً یک نوع سند را انتخاب کنید',
    docTypeChangeTitle: 'تغییر نوع سند',
    docTypeSelectWarning: 'اگر نوع سند تغییر کند، متادیتای پر شده فعلی دیگر حفظ نخواهد شد',
    firstMetaAction: 'بزن بریم',
    placeholder: {
      add: 'اضافه کردن ',
      select: 'انتخاب ',
    },
    source: {
      upload_file: 'بارگذاری فایل',
      notion: 'همگام‌سازی از Notion',
      github: 'همگام‌سازی از Github',
    },
    type: {
      book: 'کتاب',
      webPage: 'صفحه وب',
      paper: 'مقاله',
      socialMediaPost: 'پست شبکه‌های اجتماعی',
      personalDocument: 'سند شخصی',
      businessDocument: 'سند تجاری',
      IMChat: 'چت IM',
      wikipediaEntry: 'ورودی ویکی‌پدیا',
      notion: 'همگام‌سازی از Notion',
      github: 'همگام‌سازی از Github',
      technicalParameters: 'پارامترهای فنی',
    },
    field: {
      processRule: {
        processDoc: 'پردازش سند',
        segmentRule: 'قانون قطعه‌بندی',
        segmentLength: 'طول قطعات',
        processClean: 'تمیز کردن پردازش متن',
      },
      book: {
        title: 'عنوان',
        language: 'زبان',
        author: 'نویسنده',
        publisher: 'ناشر',
        publicationDate: 'تاریخ انتشار',
        ISBN: 'ISBN',
        category: 'دسته‌بندی',
      },
      webPage: {
        title: 'عنوان',
        url: 'URL',
        language: 'زبان',
        authorPublisher: 'نویسنده/ناشر',
        publishDate: 'تاریخ انتشار',
        topicsKeywords: 'موضوعات/کلیدواژه‌ها',
        description: 'توضیحات',
      },
      paper: {
        title: 'عنوان',
        language: 'زبان',
        author: 'نویسنده',
        publishDate: 'تاریخ انتشار',
        journalConferenceName: 'نام ژورنال/کنفرانس',
        volumeIssuePage: 'جلد/شماره/صفحه',
        DOI: 'DOI',
        topicsKeywords: 'موضوعات/کلیدواژه‌ها',
        abstract: 'چکیده',
      },
      socialMediaPost: {
        platform: 'پلتفرم',
        authorUsername: 'نویسنده/نام کاربری',
        publishDate: 'تاریخ انتشار',
        postURL: 'URL پست',
        topicsTags: 'موضوعات/برچسب‌ها',
      },
      personalDocument: {
        title: 'عنوان',
        author: 'نویسنده',
        creationDate: 'تاریخ ایجاد',
        lastModifiedDate: 'تاریخ آخرین ویرایش',
        documentType: 'نوع سند',
        tagsCategory: 'برچسب‌ها/دسته‌بندی',
      },
      businessDocument: {
        title: 'عنوان',
        author: 'نویسنده',
        creationDate: 'تاریخ ایجاد',
        lastModifiedDate: 'تاریخ آخرین ویرایش',
        documentType: 'نوع سند',
        departmentTeam: 'دپارتمان/تیم',
      },
      IMChat: {
        chatPlatform: 'پلتفرم چت',
        chatPartiesGroupName: 'طرفین چت/نام گروه',
        participants: 'شرکت‌کنندگان',
        startDate: 'تاریخ شروع',
        endDate: 'تاریخ پایان',
        topicsKeywords: 'موضوعات/کلیدواژه‌ها',
        fileType: 'نوع فایل',
      },
      wikipediaEntry: {
        title: 'عنوان',
        language: 'زبان',
        webpageURL: 'URL صفحه وب',
        editorContributor: 'ویرایشگر/همکار',
        lastEditDate: 'تاریخ آخرین ویرایش',
        summaryIntroduction: 'خلاصه/مقدمه',
      },
      notion: {
        title: 'عنوان',
        language: 'زبان',
        author: 'نویسنده',
        createdTime: 'زمان ایجاد',
        lastModifiedTime: 'زمان آخرین ویرایش',
        url: 'URL',
        tag: 'برچسب',
        description: 'توضیحات',
      },
      github: {
        repoName: 'نام مخزن',
        repoDesc: 'توضیحات مخزن',
        repoOwner: 'مالک مخزن',
        fileName: 'نام فایل',
        filePath: 'مسیر فایل',
        programmingLang: 'زبان برنامه‌نویسی',
        url: 'URL',
        license: 'مجوز',
        lastCommitTime: 'زمان آخرین کامیت',
        lastCommitAuthor: 'نویسنده آخرین کامیت',
      },
      originInfo: {
        originalFilename: 'نام فایل اصلی',
        originalFileSize: 'اندازه فایل اصلی',
        uploadDate: 'تاریخ بارگذاری',
        lastUpdateDate: 'تاریخ آخرین بروزرسانی',
        source: 'منبع',
      },
      technicalParameters: {
        segmentSpecification: 'مشخصات قطعات',
        segmentLength: 'طول قطعات',
        avgParagraphLength: 'طول متوسط پاراگراف',
        paragraphs: 'پاراگراف‌ها',
        hitCount: 'تعداد بازیابی',
        embeddingTime: 'زمان جاسازی',
        embeddedSpend: 'هزینه جاسازی',
      },
    },
    languageMap: {
      zh: 'چینی',
      en: 'انگلیسی',
      es: 'اسپانیایی',
      fr: 'فرانسوی',
      de: 'آلمانی',
      ja: 'ژاپنی',
      ko: 'کره‌ای',
      ru: 'روسی',
      ar: 'عربی',
      pt: 'پرتغالی',
      it: 'ایتالیایی',
      nl: 'هلندی',
      pl: 'لهستانی',
      sv: 'سوئدی',
      tr: 'ترکی',
      he: 'عبری',
      hi: 'هندی',
      da: 'دانمارکی',
      fi: 'فنلاندی',
      no: 'نروژی',
      hu: 'مجاری',
      el: 'یونانی',
      cs: 'چکی',
      th: 'تایلندی',
      id: 'اندونزیایی',
    },
    categoryMap: {
      book: {
        fiction: 'داستان',
        biography: 'زندگی‌نامه',
        history: 'تاریخ',
        science: 'علم',
        technology: 'فناوری',
        education: 'آموزش',
        philosophy: 'فلسفه',
        religion: 'دین',
        socialSciences: 'علوم اجتماعی',
        art: 'هنر',
        travel: 'سفر',
        health: 'سلامت',
        selfHelp: 'خودیاری',
        businessEconomics: 'اقتصاد کسب‌وکار',
        cooking: 'آشپزی',
        childrenYoungAdults: 'کودکان و نوجوانان',
        comicsGraphicNovels: 'کمیک‌ها و رمان‌های گرافیکی',
        poetry: 'شعر',
        drama: 'نمایشنامه',
        other: 'دیگر',
      },
      personalDoc: {
        notes: 'یادداشت‌ها',
        blogDraft: 'پیش‌نویس وبلاگ',
        diary: 'دفتر خاطرات',
        researchReport: 'گزارش پژوهش',
        bookExcerpt: 'گزیده کتاب',
        schedule: 'برنامه‌ریزی',
        list: 'فهرست',
        projectOverview: 'نمای کلی پروژه',
        photoCollection: 'مجموعه عکس',
        creativeWriting: 'نوشته خلاقانه',
        codeSnippet: 'قطعه کد',
        designDraft: 'پیش‌نویس طراحی',
        personalResume: 'رزومه شخصی',
        other: 'دیگر',
      },
      businessDoc: {
        meetingMinutes: 'صورتجلسه',
        researchReport: 'گزارش پژوهش',
        proposal: 'پیشنهاد',
        employeeHandbook: 'راهنمای کارمند',
        trainingMaterials: 'مواد آموزشی',
        requirementsDocument: 'سند نیازمندی‌ها',
        designDocument: 'سند طراحی',
        productSpecification: 'مشخصات محصول',
        financialReport: 'گزارش مالی',
        marketAnalysis: 'تحلیل بازار',
        projectPlan: 'طرح پروژه',
        teamStructure: 'ساختار تیم',
        policiesProcedures: 'سیاست‌ها و رویه‌ها',
        contractsAgreements: 'قراردادها و توافق‌نامه‌ها',
        emailCorrespondence: 'مکاتبات ایمیلی',
        other: 'دیگر',
      },
    },
  },
  embedding: {
    processing: 'در حال پردازش جاسازی...',
    paused: 'جاسازی متوقف شده',
    completed: 'جاسازی کامل شد',
    error: 'خطای جاسازی',
    docName: 'پیش‌پردازش سند',
    mode: 'قانون بخش‌بندی',
    segmentLength: 'طول قطعات',
    textCleaning: 'پیش‌تعریف و تمیز کردن متن',
    segments: 'پاراگراف‌ها',
    highQuality: 'حالت با کیفیت بالا',
    economy: 'حالت اقتصادی',
    estimate: 'مصرف تخمینی',
    stop: 'توقف پردازش',
    resume: 'ادامه پردازش',
    automatic: 'خودکار',
    custom: 'سفارشی',
    previewTip: 'پیش‌نمایش پاراگراف پس از اتمام جاسازی در دسترس خواهد بود',
  },
  segment: {
    paragraphs: 'پاراگراف‌ها',
    keywords: 'کلیدواژه‌ها',
    addKeyWord: 'اضافه کردن کلیدواژه',
    keywordError: 'حداکثر طول کلیدواژه ۲۰ کاراکتر است',
    characters: 'کاراکترها',
    hitCount: 'تعداد بازیابی',
    vectorHash: 'هش برداری: ',
    questionPlaceholder: 'سؤال را اینجا اضافه کنید',
    questionEmpty: 'سؤال نمی‌تواند خالی باشد',
    answerPlaceholder: 'پاسخ را اینجا اضافه کنید',
    answerEmpty: 'پاسخ نمی‌تواند خالی باشد',
    contentPlaceholder: 'محتوا را اینجا اضافه کنید',
    contentEmpty: 'محتوا نمی‌تواند خالی باشد',
    newTextSegment: 'قطعه متن جدید',
    newQaSegment: 'قطعه پرسش و پاسخ جدید',
    delete: 'حذف این قطعه؟',
  },
}

export default translation