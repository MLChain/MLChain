const translation = {
  title: 'Araçlar',
  createCustomTool: 'Özel Araç Oluştur',
  customToolTip: 'Mlchain özel araçları hakkında daha fazla bilgi edinin',
  type: {
    all: 'Hepsi',
    builtIn: 'Yerleşik',
    custom: 'Özel',
    workflow: 'Workflow',
  },
  contribute: {
    line1: 'Mlchain\'ye ',
    line2: 'araçlar eklemekle ilgileniyorum.',
    viewGuide: 'Rehberi Görüntüle',
  },
  author: 'Tarafından',
  auth: {
    unauthorized: 'Yetki Ver',
    authorized: 'Yetkilendirildi',
    setup: 'Kullanmak için yetkilendirmeyi ayarla',
    setupModalTitle: 'Yetkilendirmeyi Ayarla',
    setupModalTitleDescription: 'Kimlik bilgilerini yapılandırdıktan sonra, çalışma alanındaki tüm üyeler uygulamaları düzenlerken bu aracı kullanabilir.',
  },
  includeToolNum: '{{num}} araç dahil',
  addTool: 'Araç Ekle',
  addToolModal: {
    type: 'Tür',
    category: 'Kategori',
    add: 'Ekle',
    added: 'Eklendi',
    manageInTools: 'Araçlarda Yönet',
    emptyTitle: 'Kullanılabilir workflow aracı yok',
    emptyTip: 'Git "Workflow -> Araç olarak Yayınla"',
  },
  createTool: {
    title: 'Özel Araç Oluştur',
    editAction: 'Yapılandır',
    editTitle: 'Özel Aracı Düzenle',
    name: 'İsim',
    toolNamePlaceHolder: 'Araç ismini girin',
    nameForToolCall: 'Araç çağrı adı',
    nameForToolCallPlaceHolder: 'Makine tanıması için kullanılır, örneğin getCurrentWeather, list_pets',
    nameForToolCallTip: 'Sadece rakamlar, harfler ve alt çizgileri destekler.',
    description: 'Açıklama',
    descriptionPlaceholder: 'Araç amacının kısa açıklaması, örneğin belirli bir yer için sıcaklığı al.',
    schema: 'Şema',
    schemaPlaceHolder: 'OpenAPI şemanızı buraya girin',
    viewSchemaSpec: 'OpenAPI-Swagger Spesifikasyonunu Görüntüle',
    importFromUrl: 'URL\'den İçe Aktar',
    importFromUrlPlaceHolder: 'https://...',
    urlError: 'Geçerli bir URL girin',
    examples: 'Örnekler',
    exampleOptions: {
      json: 'Hava Durumu (JSON)',
      yaml: 'Evcil Hayvan Mağazası (YAML)',
      blankTemplate: 'Boş Şablon',
    },
    availableTools: {
      title: 'Kullanılabilir Araçlar',
      name: 'İsim',
      description: 'Açıklama',
      method: 'Yöntem',
      path: 'Yol',
      action: 'Eylemler',
      test: 'Test',
    },
    authMethod: {
      title: 'Yetkilendirme yöntemi',
      type: 'Yetkilendirme türü',
      keyTooltip: 'Http Başlığı Anahtarı, ne olduğunu bilmiyorsanız "Authorization" olarak bırakabilirsiniz veya özel bir değere ayarlayabilirsiniz',
      types: {
        none: 'Yok',
        api_key: 'API Anahtarı',
        apiKeyPlaceholder: 'API Anahtarı için HTTP başlık adı',
        apiValuePlaceholder: 'API Anahtarını girin',
      },
      key: 'Anahtar',
      value: 'Değer',
    },
    authHeaderPrefix: {
      title: 'Yetki Türü',
      types: {
        basic: 'Temel',
        bearer: 'Bearer',
        custom: 'Özel',
      },
    },
    privacyPolicy: 'Gizlilik politikası',
    privacyPolicyPlaceholder: 'Gizlilik politikasını girin',
    toolInput: {
      title: 'Araç Girişi',
      name: 'İsim',
      required: 'Gerekli',
      method: 'Yöntem',
      methodSetting: 'Ayar',
      methodSettingTip: 'Kullanıcı araç yapılandırmasını doldurur',
      methodParameter: 'Parametre',
      methodParameterTip: 'Çıkarım sırasında LLM tarafından doldurulur',
      label: 'Etiketler',
      labelPlaceholder: 'Etiketleri seç (isteğe bağlı)',
      description: 'Açıklama',
      descriptionPlaceholder: 'Parametrenin anlamının açıklaması',
    },
    customDisclaimer: 'Özel feragatname',
    customDisclaimerPlaceholder: 'Özel feragatnameyi girin',
    confirmTitle: 'Kaydetmek için onaylıyor musunuz?',
    confirmTip: 'Bu aracı kullanan uygulamalar etkilenecek',
    deleteToolConfirmTitle: 'Bu Aracı silmek istiyor musunuz?',
    deleteToolConfirmContent: 'Aracın silinmesi geri alınamaz. Kullanıcılar artık aracınıza erişemeyecek.',
  },
  test: {
    title: 'Test',
    parametersValue: 'Parametreler ve Değer',
    parameters: 'Parametreler',
    value: 'Değer',
    testResult: 'Test Sonuçları',
    testResultPlaceholder: 'Test sonucu burada gösterilecektir',
  },
  thought: {
    using: 'Kullanılıyor',
    used: 'Kullanıldı',
    requestTitle: 'İstek',
    responseTitle: 'Yanıt',
  },
  setBuiltInTools: {
    info: 'Bilgi',
    setting: 'Ayar',
    toolDescription: 'Araç açıklaması',
    parameters: 'parametreler',
    string: 'string',
    number: 'numara',
    required: 'Gerekli',
    infoAndSetting: 'Bilgi ve Ayarlar',
  },
  noCustomTool: {
    title: 'Özel araç yok!',
    content: 'AI uygulamaları oluşturmak için özel araçlarınızı buraya ekleyin ve yönetin.',
    createTool: 'Araç Oluştur',
  },
  noSearchRes: {
    title: 'Üzgünüz, sonuç bulunamadı!',
    content: 'Aramanızla eşleşen araçlar bulamadık.',
    reset: 'Aramayı Sıfırla',
  },
  builtInPromptTitle: 'Prompt',
  toolRemoved: 'Araç kaldırıldı',
  notAuthorized: 'Araç yetkilendirilmedi',
  howToGet: 'Nasıl alınır',
  openInStudio: 'Studyoda Aç',
  toolNameUsageTip: 'Agent akıl yürütme ve prompt için araç çağrı adı',
}

export default translation