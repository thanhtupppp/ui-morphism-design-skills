# Swiss Editorial platform mappings

| Role | HTML/CSS and React | Flutter | React Native |
|---|---|---|---|
| Publication structure | Section, header, nav, article, headings | Scaffold, ListView, semantic headers | ScrollView, View, header-role Text |
| Editorial grid | CSS Grid; same DOM order at every width | LayoutBuilder and bounded content width | onLayout and available-width padding |
| Search | Label and search input | TextField with labelText | Visible Text label and named TextInput |
| Category state | Button with aria-pressed and check mark | FilterChip with selected state | Pressable with selected accessibilityState |
| Bookmark | Native button, aria-pressed, Save/Saved text | OutlinedButton with selected Semantics | Pressable with selected accessibilityState |
| Text and surface | Namespaced CSS tokens | ThemeData colorScheme and textTheme | Local semantic palette selected by explicit theme or useColorScheme |
| Target and focus | 48px minimum, visible outline | 48px minimum, standard focus behavior | minHeight/minWidth 48, explicit focus border |

Required capabilities are semantic roles, state, focus, readable opaque surfaces, and responsive adaptation. Preferred capabilities are wide-screen asymmetry and generous typography. Optional custom fonts and decorative numerals fall back to system text and ordinary spacing.

## Implementation seeds

- Web: copy `example.tsx` with `example.css`; mount `SwissEditorialExample`. Import React hooks as shown. The local preview renders this exact component, not a separate mockup.
- Flutter: use `SwissEditorialExample` as the home of a MaterialApp. The widget inherits light/dark and high-contrast colors from the host theme. Search and local bookmark state are interactive; dispose the search controller with the widget.
- React Native: mount `SwissEditorialNativeExample` in the host safe-area container. It measures its own available width with `onLayout`, uses system font scaling, and accepts `theme="light"` or `theme="dark"` to override the OS preference. Search, category, and bookmark state stay local.

Web supports inline article disclosure; native seeds show the short body directly. This changes the presentation, not the reading hierarchy or the bookmark semantics. All renderers combine title/summary search with category filtering and expose an empty state plus reset.

## Performance and fallback

There are no third-party visual dependencies or expensive materials. Reduced-motion mode requires no alternate animation implementation. If the grid or optional font is unavailable, use a single column of system text and native controls. Maintain the same article order, names, states, and target size. For native high contrast, use the host's platform accessibility theme and verify it on a device; CSS forced-colors behavior is not a native API.

The preview exercises browser semantics and responsive behavior. Static analysis and type checks do not establish native screen-reader, hardware keyboard, or text-scaling correctness; see `verification.md` before claiming production readiness.
